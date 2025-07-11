from pydantic import BaseModel

class MessageRequest(BaseModel):
    sender: str
    message: str

class MessageResponse(BaseModel):
    sender: str
    message: str