from openai import OpenAI
import asyncio

client = OpenAI(
    api_key="sk-uLBEI9VIHqTLBJ5RJoVWewWF7cY3Z6qCf0pxDRRwVC3b9QxF",
    base_url="https://api.moonshot.cn/v1",
)


async def steam():
    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        stream=True,
        messages=[{
            "role":
            "system",
            "content":
            "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。"
        }, {
            "role": "user",
            "content": "你好，我叫李雷，1+1等于多少？"
        }],
        temperature=0.3,
    )
    return completion.choices[0].message.content


async def main():
    task = asyncio.create_task(steam())
    res1 = await task
    print(res1)

asyncio.run(main())