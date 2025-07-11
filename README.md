# Simple Chatbot

A full-stack chatbot application featuring a Korean language model (KoGPT2) with real-time streaming responses. The project consists of a React frontend, Spring Boot backend, and a Python FastAPI service for AI model inference.

## 🚀 Features

- **Real-time Chat Interface**: Modern React-based chat UI with streaming responses
- **Korean Language Model**: Powered by fine-tuned KoGPT2 for natural Korean conversations
- **WebSocket Communication**: Real-time bidirectional communication between frontend and backend
- **Streaming Responses**: Word-by-word response generation for better user experience
- **Multi-Architecture**: Microservices architecture with separate frontend, backend, and AI service

## 🏗️ Architecture

```
Simple_Chatbot/
├── frontend/          # React application (UI)
├── backend/           # Spring Boot application (WebSocket server)
└── markov/            # Python FastAPI service (AI model inference)
```

### Components

- **Frontend (React)**: User interface with real-time chat functionality
- **Backend (Spring Boot)**: WebSocket server handling real-time communication
- **AI Service (FastAPI)**: KoGPT2 model inference with streaming responses

## 🛠️ Tech Stack

### Frontend
- React 19.1.0
- WebSocket API
- Axios for HTTP requests
- Modern CSS styling

### Backend
- Spring Boot 3.4.4
- Java 17
- WebSocket support
- Spring WebFlux

### AI Service
- FastAPI
- PyTorch
- Transformers (Hugging Face)
- KoGPT2 model

## 📋 Prerequisites

- Node.js (v16 or higher)
- Java 17
- Python 3.11
- Git

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Simple_Chatbot
```

### 2. Frontend Setup

```bash
cd frontend
npm install
npm start
```

The React app will run on `http://localhost:3000`

### 3. Backend Setup

```bash
cd backend
./gradlew bootRun
```

The Spring Boot server will run on `http://localhost:8080`

### 4. AI Service Setup

```bash
cd markov
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

The FastAPI service will run on `http://localhost:8000`

## 🎯 Usage

1. Start all three services (frontend, backend, AI service)
2. Open your browser and navigate to `http://localhost:3000`
3. Start chatting with the Korean language model
4. Enjoy real-time streaming responses!

## 📁 Project Structure

```
Simple_Chatbot/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatBot.js      # Main chat component
│   │   │   └── ChatBot.css     # Chat styling
│   │   ├── api/
│   │   │   └── chatApi.js      # API utilities
│   │   └── App.js              # Main app component
│   └── package.json
├── backend/
│   ├── src/main/java/
│   │   └── com/example/        # Spring Boot application
│   ├── build.gradle
│   └── application.properties
├── markov/
│   ├── app/
│   │   ├── main.py             # FastAPI application
│   │   ├── chatbot.py          # Chatbot logic
│   │   └── schemas.py          # Pydantic models
│   ├── data/                   # Training data
│   ├── final/                  # Trained model
│   └── requirements.txt
└── README.md
```

## 🔧 Configuration

### Environment Variables

Create `.env` files in respective directories if needed:

**Frontend (.env)**
```
REACT_APP_API_URL=http://localhost:8080
REACT_APP_WS_URL=ws://localhost:8080/ws/chat
```

**Backend (application.properties)**
```properties
server.port=8080
spring.websocket.max-text-message-size=8192
```

**AI Service (.env)**
```
MODEL_PATH=./final
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [KoGPT2](https://github.com/SKT-AI/KoGPT2) - Korean language model
- [Hugging Face Transformers](https://huggingface.co/transformers/) - Model framework
- [Spring Boot](https://spring.io/projects/spring-boot) - Backend framework
- [React](https://reactjs.org/) - Frontend framework

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Happy Chatting! 👽✨** 