import streamlit as st
from dotenv import load_dotenv
from agent import agent

load_dotenv()

st.set_page_config(page_title="GlowTouch Makeup Assistant", page_icon="💄", layout="wide")

st.title("💄 GlowTouch Makeup Assistant")
st.caption("Ask about products, check stock, get skin-type recommendations, or place an order.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("e.g., Show me lipsticks / I have oily skin, what do you recommend? / Order 1 Hydrating Foundation"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Checking products..."):
            try:
                response = agent.run(prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Error: {e}")

# Sidebar
with st.sidebar:
    st.header("📋 Quick Actions")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.caption("GlowTouch · AI Makeup Assistant")