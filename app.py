import streamlit as st
from chatbot import get_answer

st.title("Mini Chatbot FAQ")


if 'history' not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Posez votre question :")
if user_input:
    response = get_answer(user_input)
    st.session_state.history.append(("Vous", user_input))
    st.session_state.history.append(("Bot", response))

# Afficher l'historique
for sender, message in st.session_state.history:
    st.write(f"**{sender} :** {message}")

if st.button("Effacer la conversation"):
    st.session_state.history = []