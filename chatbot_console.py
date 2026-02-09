from chatbot.core import ChatBot

bot = ChatBot()

if __name__ == "__main__":
    print("Welcome to Mini FAQ Chatbot! (type 'quit' to exit)")
    while True:
        q = input("You: ")
        if q.lower() == 'quit':
            break
        questions = q.split(";")
        for question in questions:
            print("Bot:", bot.get_answer(question.strip()))
