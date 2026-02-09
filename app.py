import streamlit as st
from chatbot.core_groq import ChatBotGroq
from chatbot.session import ChatSession
import pandas as pd

bot = ChatBotGroq()

if "session" not in st.session_state:
    st.session_state.session = ChatSession()

st.title("Mini FAQ Chatbot with Groq 🤖")

user_input = st.text_input("Ask your question:")

if user_input:
    response = bot.get_answer(user_input)
    st.session_state.session.add_message("You", user_input)
    st.session_state.session.add_message("Bot", response)

for sender, message in st.session_state.session.history:
    if sender == "You":
        st.markdown(f"**👤 {sender}:** {message}")
    else:
        st.markdown(f"**🤖 {sender}:** {message}")

if st.button("Clear Conversation"):
    st.session_state.session.clear()

# Export chat history
if st.button("Export Conversation"):
    if st.session_state.session.history:
        df = pd.DataFrame(st.session_state.session.history, columns=["Sender", "Message"])
        df.to_csv("logs/exported_chat.csv", index=False)
        st.success("Conversation exported to logs/exported_chat.csv")
    else:
        st.warning("No conversation to export yet!")
