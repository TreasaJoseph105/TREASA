import requests
import json

API_KEY = "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"
URL = "https://openrouter.ai/api/v1/chat/completions"

user_input = input("Ask a question: ")

messages = [
    {
        "role": "system",
        "content": (
            "You are an IT engineer assistant. "
            "Answer only IT and computer-related content. "
            "If the question is not IT-related, respond with: "
            "'Only IT and computer-related questions are answered. I am an IT engineer.'"
        )
    },
    {
        "role": "user",
        "content": user_input
    }
]

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "IT-Chatbot"
}

data = {
    "model": "openai/gpt-4o-mini",
    "messages": messages,
    "temperature": 0,
    "max_tokens": 150
}

response = requests.post(URL, headers=headers, data=json.dumps(data))

print(response.json()["choices"][0]["message"]["content"])
