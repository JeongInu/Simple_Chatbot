package com.example.backend.websocket;

import com.example.backend.service.ChatService;
import lombok.NonNull;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Component;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.socket.CloseStatus;
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketSession;
import org.springframework.web.socket.handler.TextWebSocketHandler;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

@Component
public class ChatWebSocketHandler extends TextWebSocketHandler {

//  private final WebClient webClient = WebClient.create("http://127.0.0.1:8000");
//
//  @Override
//  public void handleTextMessage(@NonNull WebSocketSession session, TextMessage message) {
//    String userInput = message.getPayload();
//
//    // 클라이언트로부터 받은 메시지를 Flask API로 전달
//    webClient.post()
//            .uri("/api/chat")
//            .contentType(MediaType.APPLICATION_JSON)
//            .accept(MediaType.TEXT_EVENT_STREAM)
//            .bodyValue(Map.of("sender", "user", "message", userInput))
//            .retrieve()
//            .bodyToFlux(String.class)
//            .doOnTerminate(() -> {
//              // 응답이 끝난 후 대기 상태를 해제
//              session.getAttributes().put("waitingForResponse", false);
//            })
//            .subscribe(chunk -> {
//              try {
//                // Flask 서버로부터 받은 스트리밍 데이터를 WebSocket 클라이언트로 전송
//                session.sendMessage(new TextMessage(chunk));
//              } catch (Exception e) {
//                e.printStackTrace();
//              }
//            });
//  }

  private final ChatService chatService;
  private final Map<WebSocketSession, Boolean> sessionStream = new ConcurrentHashMap<>();
  private static Logger logger = LoggerFactory.getLogger(ChatWebSocketHandler.class);

  public ChatWebSocketHandler(ChatService chatService) {
    this.chatService = chatService;
  }

  @Override
  public void handleTextMessage(@NonNull WebSocketSession session, @NonNull TextMessage message) throws Exception {
    String userInput = message.getPayload();

    if(sessionStream.getOrDefault(session, false)) {
      session.sendMessage(new TextMessage("👽 아직 응답 중이에요!"));
      return;
    }

    sessionStream.put(session, true);

    Flux<String> responseFlux = chatService.toModel(userInput);

    responseFlux
            .doOnNext(token -> {
              try{
                session.sendMessage(new TextMessage(token));
              }catch (Exception e){
                e.printStackTrace();
              }
            })
            .doFinally(signalType -> {
              try {
                //  응답 종료 신호 보내기
                logger.info("응답 끝 - SOCKET_CLOSE");
                String endMessage = "{\"message\":\"SOCKET_CLOSE\"}";
                session.sendMessage(new TextMessage(endMessage));
                sessionStream.put(session, false);
              } catch (Exception e) {
                e.printStackTrace();
              }
              sessionStream.put(session, false);
            })
            .subscribe();
  }

  @Override
  public void afterConnectionClosed(@NonNull WebSocketSession session, @NonNull CloseStatus status) throws Exception {
    sessionStream.remove(session);
  }

}
