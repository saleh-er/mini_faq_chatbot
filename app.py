import streamlit as st
from chatbot.core import ChatBot
from chatbot.session import ChatSession
import pandas as pd

bot = ChatBot()

if 'session' not in st.session_state:
    st.session_state.session = ChatSession()

st.title("Mini FAQ Chatbot")

user_input = st.text_input("Ask your question:")
if user_input:
    response = bot.get_answer(user_input)
    st.session_state.session.add_message("You", user_input)
    st.session_state.session.add_message("Bot", response)

# Display chat history
for sender, message in st.session_state.session.history:
    st.write(f"**{sender}:** {message}")

# Clear conversation
if st.button("Clear Conversation"):
    st.session_state.session.clear()

# Export chat history
if st.button("Export Conversation"):
    df = pd.DataFrame(st.session_state.session.history, columns=["Sender", "Message"])
    df.to_csv("logs/exported_chat.csv", index=False)
    st.success("Conversation exported to logs/exported_chat.csv")
