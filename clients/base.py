from abc import ABC, abstractmethod
#3 define la interfaz que debe cumplir cualquier cliente llm
from schemas import ChatMessage, ModelResponse

# toma los esquemas y hace que se cumplan se hereden
class BaseLLMClient(ABC):
    @abstractmethod
    async def generate(self, messages: list[ChatMessage]) -> ModelResponse:
        """Genera una respuesta completa."""
        pass

    @abstractmethod
    async def stream(self, messages: list[ChatMessage]):
        """Devuelve la respuesta en streaming."""
        pass