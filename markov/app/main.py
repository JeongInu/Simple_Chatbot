import json
import random

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from app.schemas import MessageRequest, MessageResponse
from app.chatbot import chatbot
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import time
app = FastAPI()

model_path = "./final"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)
@app.get("/")
def read_root():
    return {"message": "FastAPI Server is running"}

# def generate_response(input_text: str) -> str:
#     inputs = tokenizer(input_text, return_tensors="pt")
#     outputs = model.generate(inputs["input_ids"], max_length=100, num_return_sequences=1)
#     response = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     return response
#
# @app.post("/chat", response_model=MessageResponse)
# def chat(req: MessageRequest):
#     user_input = req.message
#     # reply = chatbot.respond(start_word=user_input if user_input else "안녕, 반가워!")
#     reply = generate_response(user_input)
#     return MessageResponse(sender="chatbot", message=reply)

@app.post("/api/chat", response_model=MessageResponse)
async def chat(req: MessageRequest):
    print("!")
    input_text = req.message
    input_user = req.sender

    def generate_stream():
        inputs = tokenizer(input_text, return_tensors="pt")
        outputs = model.generate(
            inputs["input_ids"],
            max_length=100,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.8,
            pad_token_id=tokenizer.eos_token_id
        )
        decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)

        for word in decoded.split():
            payload = MessageResponse(
                sender = input_user,
                message = word
            )
            yield json.dumps(payload.model_dump()) + "\n" # chunk 단위라 개행 포함
            time.sleep(0.3)

    return StreamingResponse(generate_stream(), media_type="application/json")