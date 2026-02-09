import streamlit as st
from chatbot import get_answer

st.title("Mini Chatbot FAQ")

user_input = st.text_input("Posez votre question :")
if user_input:
    response = get_answer(user_input)
    st.write("Bot :", response)
