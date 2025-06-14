import openai
import streamlit as st

# API key from Streamlit Secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Ninos – AI Chatbot", page_icon="🤖")
st.title("🌐 Ninos – Your Smart AI Assistant (All Languages)")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are Ninos, a helpful and intelligent assistant that understands and replies in any language the user uses."}
    ]

for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input("Talk to Ninos...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.spinner("Ninos is thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write(reply)
