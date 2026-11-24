import streamlit as st
import requests

# On EC2, if frontend and backend are in the same container, use localhost
API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="GlowTouch Makeup Assistant", page_icon="💄")
st.title("💄 GlowTouch Makeup Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("e.g., Show me lipsticks / I have oily skin, what do you recommend? / Order 1 Hydrating Foundation"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Checking products..."):
            try:
                resp = requests.post(API_URL, json={"message": prompt}, timeout=120)
                if resp.status_code == 200:
                    data = resp.json()
                    answer = data["response"]
                else:
                    answer = f"API error: {resp.status_code} - {resp.text}"
            except Exception as e:
                answer = f"Connection error: {e}"
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})