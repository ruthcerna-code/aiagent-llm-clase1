import anthropic
from schemas import ChatMessage, ModelResponse
from config import ANTHROPIC_API_KEY
from clients.base import BaseLLMClient
#Implementa la interfaz creada en base para comunicarse con la api de Anthropic (Claude)

class AnthropicClient(BaseLLMClient):
    def __init__(self, model: str = "claude-opus-5"):
        self.client = anthropic.AsyncAnthropic(api_key=ANTHROPIC_API_KEY)
        self.model = model
#Espera respuesta completa
    async def generate(self, messages: list[ChatMessage]) -> ModelResponse:
        try:
            response = await self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                messages=[
                    {"role": message.role, "content": message.content}
                    for message in messages
                ],
            )
            text = next(
                (block.text for block in response.content if block.type == "text"),
                "",
            )
            return ModelResponse(text=text)
        except Exception as e:
            return ModelResponse(text=f"Error: {e}")
#Entrega pequeños fragmentos mediante yield a medida que Claude los va generando
    async def stream(self, messages: list[ChatMessage]):
        try:
            async with self.client.messages.stream(
                model=self.model,
                max_tokens=1024,
                messages=[
                    {"role": message.role, "content": message.content}
                    for message in messages
                ],
            ) as stream:
                async for text in stream.text_stream:
                    yield text  #Como return pero devuelve un valor antes de terminar ejecucion.
        except Exception as e:
            yield f"Error: {e}"
