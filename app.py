import streamlit as st
from chatbot.core import ChatBot
from chatbot.session import ChatSession
import pandas as pd

bot = ChatBot()

# Initialisation de la session
if 'session' not in st.session_state:
    st.session_state.session = ChatSession()

st.set_page_config(page_title="Mini FAQ Chatbot", page_icon="🤖", layout="centered")
st.title("Mini FAQ Chatbot 🤖")

# Saisie de l'utilisateur
user_input = st.text_input("Ask your question:")

if user_input:
    response = bot.get_answer(user_input)
    sentiment = bot.detect_sentiment(user_input)
    st.session_state.session.add_message("You", f"{user_input} ({sentiment})")
    st.session_state.session.add_message("Bot", response)

# Affichage de l'historique avec avatars
for sender, message in st.session_state.session.history:
    if sender == "You":
        st.markdown(f"**👤 {sender}:** {message}")
    else:
        st.markdown(f"**🤖 {sender}:** {message}")

# Bouton pour effacer la conversation
if st.button("Clear Conversation"):
    st.session_state.session.clear()

# Bouton pour exporter l'historique
if st.button("Export Conversation"):
    if st.session_state.session.history:
        df = pd.DataFrame(st.session_state.session.history, columns=["Sender", "Message"])
        df.to_csv("logs/exported_chat.csv", index=False)
        st.success("Conversation exported to logs/exported_chat.csv")
    else:
        st.warning("No conversation to export yet!")
