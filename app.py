import streamlit as st
from openai import OpenAI
import os

# 🔑 Setup OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🌐 Title
st.set_page_config(page_title="Ninos – All Language AI", page_icon="🌍")
st.title("🌐 Ninos – Your Smart AI Assistant\n(All Languages)")

# 🧠 Session state for conversation
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are Ninos, a friendly and smart multilingual assistant."}
    ]

# 💬 Show chat history
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ✍️ User input
prompt = st.chat_input("Talk to Ninos...")

# 🧠 Generate AI response
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.spinner("Ninos is thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.write(reply)
