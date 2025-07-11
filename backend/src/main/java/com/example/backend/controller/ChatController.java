//package com.example.backend.controller;
//
//import com.example.backend.dto.MessageRequest;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.http.ResponseEntity;
//import org.springframework.web.bind.annotation.*;
//import org.springframework.web.reactive.function.client.WebClient;
//
//import java.util.Map;
//
//@RestController
//@RequestMapping("/api/chat")
//@CrossOrigin(origins = "http://localhost:3000")
//public class ChatController {
//
//    private final WebClient.Builder webClientBuilder;
//
//    @Autowired
//    public ChatController(WebClient.Builder webClientBuilder) {
//        this.webClientBuilder = webClientBuilder;
//    }
//
//    @PostMapping
//    public ResponseEntity<Map<String, String>> sendMessageToChatbot(@RequestBody MessageRequest request){
//        String userMessage = request.getMessage();
//        System.out.println(userMessage);
//
//        Map<String, String> response = webClientBuilder.baseUrl("http://127.0.0.1:8000/chat")
//                .build()
//                .post()
//                .bodyValue(new MessageRequest(userMessage))
//                .retrieve()
//                .bodyToMono(Map.class)
//                .block();
//
//        return ResponseEntity.ok(response);
//    }
//
//}
