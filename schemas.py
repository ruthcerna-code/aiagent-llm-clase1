from pydantic import BaseModel
# 2 Valida datos de entrada y salida con pydantic

class ChatMessage(BaseModel):
    role: str
    content: str

class ModelResponse(BaseModel):
    text: str