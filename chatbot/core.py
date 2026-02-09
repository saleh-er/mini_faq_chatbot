import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
from dotenv import load_dotenv
import os

# Charger les variables du .env
load_dotenv()

FAQ_PATH = os.getenv("FAQ_PATH", "data/faq.csv")
THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", 0.3))

class ChatBot:
    def __init__(self, faq_path=FAQ_PATH):
        self.faq = pd.read_csv(faq_path)
        self.vectorizer = TfidfVectorizer()
        self.X = self.vectorizer.fit_transform(self.faq['question'])
    
    def get_answer(self, user_question, threshold=THRESHOLD):
        user_vec = self.vectorizer.transform([user_question])
        sim_scores = cosine_similarity(user_vec, self.X)
        indices = [i for i, score in enumerate(sim_scores[0]) if score >= threshold]
        if not indices:
            return "Désolé, je n'ai pas compris votre question. Veuillez reformuler."
        return self.faq['answer'][random.choice(indices)]
