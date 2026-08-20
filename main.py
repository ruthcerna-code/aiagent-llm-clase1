import asyncio
from clients.gemini_client import GeminiClient
from clients.anthropic_client import AnthropicClient
from schemas import ChatMessage
#
async def main():
    client = GeminiClient()
    messages = [
        ChatMessage(
            role="user",
            content="¿Qué es la entropía, decimelo en una oracion?"
        )
    ]
    print("=== GEMINI: Respuesta normal ===")
    response = await client.generate(messages)
    print(response.text)
    print("\n=== GEIMINL: Streaming ===")
    async for token in client.stream(messages):
        print(token, end="", flush=True) #end dice que no espere salto de linea y flush que vacie bufer
    print()

    client = AnthropicClient()
    print("\n=== ANTHROPIC: Respuesta normal (Anthropic) ===")
    response = await client.generate(messages)
    print(response.text)
    print("\n=== ANTHROPIC: Streaming (Anthropic) ===")
    async for token in client.stream(messages):
        print(token, end="", flush=True)
    print()

if __name__ == "__main__":
    asyncio.run(main())
