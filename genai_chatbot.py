import requests
import json

API_KEY = "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"

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": msg}
        ]
    }

    r = requests.post(url, headers=headers, json=payload)

    if r.status_code == 200:
        reply = r.json()["choices"][0]["message"]["content"]
        print("AI:", reply)
    else:
        print("Error:", r.text)