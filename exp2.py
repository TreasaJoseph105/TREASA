from openai import OpenAI

# Create client properly
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"   # 🔴 Put your API key here
)

# Send request
response = client.chat.completions.create(
    model="openai/gpt-3.5-turbo",   # or any model available in OpenRouter
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

# Print response
print(response.choices[0].message.content)
