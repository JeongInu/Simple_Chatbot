# 💬 Simple Chatbot

KoGPT2 기반 실시간 스트리밍 챗봇 애플리케이션

React 프론트엔드, Spring Boot 백엔드, FastAPI 기반 AI 서버로 구성된 풀스택 한국어 챗봇 프로젝트입니다.

---

## 🚀 주요 기능

- 🗨️ **실시간 채팅 UI**: React 기반의 모던한 채팅 인터페이스  
- 🇰🇷 **한국어 언어 모델**: KoGPT2로 자연스러운 대화 테스트(성능은 좋지 안 좋음. 연동 테스트)
- 🔌 **WebSocket 실시간 통신**: 빠른 반응과 양방향 메시징 지원  
- ⏱️ **스트리밍 응답 처리**: 단어 단위 응답으로 몰입감 있는 대화  
- 🧩 **마이크로서비스 아키텍처**: 프론트 / 백엔드 / AI 서버 분리 구조  

---

## 🏗️ 시스템 구성

```
Simple_Chatbot/
├── frontend/   # React 프론트엔드
├── backend/    # Spring Boot 백엔드 (WebSocket)
└── markov/     # FastAPI 기반 AI 모델 서버
```

---

## ⚙️ 기술 스택

### 프론트엔드
- React 19.1.0  
- WebSocket API  
- Axios  
- 모던 CSS 스타일링  

### 백엔드
- Spring Boot 3.4.4  
- Java 17  
- WebSocket / WebFlux  

### AI 서비스
- FastAPI  
- PyTorch  
- Hugging Face Transformers  
- KoGPT2  

---

## 🛠️ 개발 환경

- Node.js (v16 이상)  
- Java 17  
- Python 3.11  
- Git

---

## 🚀 실행 방법

### 1. 리포지토리 클론

```bash
git clone <your-repository-url>
cd Simple_Chatbot
```

### 2. 프론트엔드 실행

```bash
cd frontend
npm install
npm start
```
> 기본 주소: `http://localhost:3000`

### 3. 백엔드 실행

```bash
cd backend
./gradlew bootRun
```
> 기본 포트: `http://localhost:8080`

### 4. AI 서비스 실행

```bash
cd markov
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
> 기본 포트: `http://localhost:8000`

---

## 💬 사용 방법

1. 프론트엔드, 백엔드, AI 서버를 모두 실행  
2. 브라우저에서 `http://localhost:3000` 접속  
3. 실시간 스트리밍 챗봇과 한국어로 대화 시작!

---
