import streamlit as st
from openai import OpenAI
import os

# 🔑 Secure API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🌍 Streamlit setup
st.set_page_config(page_title="Ninos – All Languages", page_icon="🧠")
st.title("🧠 Ninos – Your Smart AI Assistant (GPT-4o / All Languages)")

# 🧠 Memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are Ninos, a smart multilingual assistant built with GPT-4o. Be friendly and helpful."}
    ]

# 💬 Show chat history
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 🗣 User input
prompt = st.chat_input("Talk to Ninos...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.spinner("Ninos is thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4o",  # 🔁 GPT-4o here
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": reply})
            with st.chat_message("assistant"):
                st.write(reply)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
