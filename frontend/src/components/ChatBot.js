import React, { useState, useRef, useEffect } from "react";
import './ChatBot.css';

const ChatBot = () => {
  const [input, setInput] = useState("");
  const [responses, setResponses] = useState([]);
  const [streaming, setStreaming] = useState(false); // 상태로 관리
  const ws = useRef(null);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [responses]);

  useEffect(() => {
    // WebSocket 연결
    ws.current = new WebSocket("ws://localhost:8080/ws/chat");

    ws.current.onopen = () => {
      console.log("WebSocket 연결됨");
    };

    // 서버에서 메시지 수신 처리
    ws.current.onmessage = (event) => {
      let data;
      try {
        data = JSON.parse(event.data);
      } catch (err) {
        console.error("JSON 파싱 실패:", event.data);
        return;
      }

      console.log("서버로부터 받은 메시지:", data); // 서버에서 받은 전체 메시

      setStreaming(true); // 응답 중일 때 상태 업데이트

      // 메시지를 상태에 추가 (계속해서 이어붙이기)
      if (data.message !== "SOCKET_CLOSE") {
        setResponses((prev) => {
          const newResponses = [...prev];
          const lastMessage = newResponses.pop();
          const updatedMessage = {
            ...lastMessage,
            message: lastMessage.message + ' ' + data.message,
          };
          newResponses.push(updatedMessage);
          return newResponses;
        });
      }

      // 서버에서 종료 메시지 판단 (`END` 메시지나 완료된 응답 확인)
      if (data.message === "SOCKET_CLOSE") {
        console.log("응답 끝: SOCKET_CLOSE 메시지 받음!"); // __END__ 메시지를 받았을 때 로그 찍기
        setStreaming(false);
      }
    };

    // WebSocket 연결 종료 처리
    ws.current.onclose = () => {
      console.log("WebSocket 연결 종료");
    };

    return () => {
      ws.current?.close();
    };
  }, []);

  // 메시지 전송 처리
  const handleSend = () => {
    if (!input.trim() || !ws.current || ws.current.readyState !== 1 || streaming) {
      return; // 전송 불가능한 경우
    }

    // 사용자의 메시지 추가
    setResponses((prev) => [...prev, { sender: "user", message: input }]);

    // 챗봇 응답 자리 확보
    setResponses((prev) => [...prev, { sender: "chatbot", message: "" }]);

    setStreaming(true); // 응답 대기 상태로 설정
    ws.current.send(input); // WebSocket으로 메시지 전송
    setInput(""); // 입력창 초기화
  };

  return (
    <div className="container">
      <h1>👽 Streaming KoGPT2 Chatbot</h1>

      <div className="chatBox">
        {responses.map((msg, index) => (
          <div
            key={index}
            className={msg.sender === "user" ? "userMessage" : "chatbotMessage"}
          >
            <strong>{msg.sender === "user" ? "당신 😊" : "KoGPT2 👽"}: </strong>
            {msg.message}
          </div>
        ))}
        <div ref={messagesEndRef}></div>
      </div>

      <textarea
        rows={3}
        placeholder={streaming ? "응답이 끝날 때까지 기다려주세요..." : "메세지를 입력해주세요."}
        value={input}
        onChange={(event) => setInput(event.target.value)}
        onKeyDown={(event) => {
          if (event.key === "Enter" && !event.shiftKey && !event.nativeEvent.isComposing) {
            event.preventDefault();
            handleSend();
          }
        }}
        className="textarea"
        disabled={streaming} // 입력창 비활성화
      />
      <br />
      <button
        type="button"
        onClick={handleSend}
        className="button"
        disabled={streaming} // 버튼도 비활성화
      >
        {streaming ? "답변 생성 중..." : "대화하기"}
      </button>
    </div>
  );
};

export default ChatBot;
