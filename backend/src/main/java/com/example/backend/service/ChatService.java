package com.example.backend.service;

import com.example.backend.websocket.ChatWebSocketHandler;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Flux;

import java.util.HashMap;
import java.util.Map;

@Service
public class ChatService {

//    public ResponseEntity<Map<String, String>> getAnswer(String msg){
//        String reply = msg + " 👽";
//
//        Map<String, String> response = new HashMap<>();
//        response.put("sender", "chatbot");
//        response.put("reply", reply);
//        System.out.println(response);
//        return ResponseEntity.ok(response);
//    }

    private final WebClient webClient;

    public ChatService(WebClient.Builder builder) {
        this.webClient = builder
                            .baseUrl("http://127.0.0.1:8000").build();
    }

    public Flux<String> toModel(String userInput){
        return webClient.post()
                .uri("/api/chat")
                .bodyValue(Map.of("sender", "user", "message", userInput))
                .retrieve()
                .bodyToFlux(String.class);
    }

}
