from chatbot.core import ChatBot

bot = ChatBot()

if __name__ == "__main__":
    print("Bienvenue dans le Mini Chatbot FAQ ! (tapez 'quit' pour quitter)")
    while True:
        q = input("Vous : ")
        if q.lower() == 'quit':
            break
        questions = q.split(";")
        for question in questions:
            print("Bot :", bot.get_answer(question.strip()))
