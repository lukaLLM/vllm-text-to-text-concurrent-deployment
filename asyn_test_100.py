
import asyncio
import time
from openai import AsyncOpenAI

QUESTIONS_FILE = "questions_to_AI.txt"
RESULTS_FILE = "responses_results.txt"

async def send_request(client, question, idx):
    start = time.time()
    response = await client.chat.completions.create(
        model="HuggingFaceTB/SmolLM2-360M-Instruct",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."}, # Change prompt 
            {"role": "user", "content": question}
        ],
        max_tokens=500,
    )
    elapsed_ms = (time.time() - start) * 1000
    return {
        "idx": idx,
        "question": question,
        "answer": response.choices[0].message.content,
        "elapsed_ms": elapsed_ms
    }

async def main():
    # Read questions
    with open(QUESTIONS_FILE, "r") as f:
        questions = [line.strip() for line in f if line.strip()]

    client = AsyncOpenAI(
        api_key="EMPTY",
        base_url="http://localhost:8001/v1",
    )
    tasks = [send_request(client, q, i+1) for i, q in enumerate(questions)]
    results = await asyncio.gather(*tasks)

    total_time = 0
    longest = None
    for r in results:
        print(f"[{r['idx']}] Q: {r['question']}\nA: {r['answer']}\nTime: {r['elapsed_ms']:.2f} ms\n")
        total_time += r['elapsed_ms']
        if longest is None or r['elapsed_ms'] > longest:
            longest = r['elapsed_ms']
    avg_time = total_time / len(results) if results else 0
    print(f"Average response time: {avg_time:.2f} ms")
    print(f"Longest response time: {longest:.2f} ms")
if __name__ == "__main__":
    asyncio.run(main())
