from chatbot.core_groq import ChatBotGroq

bot = ChatBotGroq()

if __name__ == "__main__":
    print("Welcome to Mini FAQ Chatbot with Groq! (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        print("Bot:", bot.get_answer(user_input))
