import streamlit as st
from openai import OpenAI

# Create OpenRouter client
client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

st.title("My AI Chatbot 🤖")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from OpenRouter
    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)
