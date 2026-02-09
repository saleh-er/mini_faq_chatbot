import streamlit as st
from chatbot.core import ChatBot
from chatbot.session import ChatSession

bot = ChatBot()

if 'session' not in st.session_state:
    st.session_state.session = ChatSession()

st.title("Mini Chatbot FAQ")

user_input = st.text_input("Posez votre question :")
if user_input:
    response = bot.get_answer(user_input)
    st.session_state.session.add_message("Vous", user_input)
    st.session_state.session.add_message("Bot", response)

# Afficher l'historique
for sender, message in st.session_state.session.history:
    st.write(f"**{sender} :** {message}")

if st.button("Effacer la conversation"):
    st.session_state.session.clear()
