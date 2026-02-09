import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Charger la FAQ
faq = pd.read_csv('data/faq.csv')

# Vectoriser les questions
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(faq['question'])

def get_answer(user_question):
    user_vec = vectorizer.transform([user_question])
    sim_scores = cosine_similarity(user_vec, X)
    index = sim_scores.argmax()
    return faq['answer'][index]

# Chatbot en console
if __name__ == "__main__":
    print("Bienvenue dans le Mini Chatbot FAQ ! (tapez 'quit' pour quitter)")
    while True:
        q = input("Vous : ")
        if q.lower() == 'quit':
            break
        print("Bot :", get_answer(q))
