import asyncio
import time
from openai import AsyncOpenAI

async def main():
    client = AsyncOpenAI(
        api_key="EMPTY",  # vLLM does not require a real key by default
        base_url="http://localhost:8001/v1",  # Change if your server is remote
    )
    start = time.time()
    response = await client.chat.completions.create(
        model="HuggingFaceTB/SmolLM2-360M-Instruct",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": "Why are you so Smol? "}
        ],
        max_tokens=500
    )
    elapsed_ms = (time.time() - start) * 1000
    print(response.choices[0].message.content)
    print(f"Response time: {elapsed_ms:.2f} ms")

asyncio.run(main())

# http://localhost:8001/v1/docs
