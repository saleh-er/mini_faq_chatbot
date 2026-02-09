import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
from chatbot.llm import query_groq
from chatbot.utils import clean_text
from dotenv import load_dotenv
import os

load_dotenv()

FAQ_PATH = os.getenv("FAQ_PATH", "data/faq.csv")
THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", 0.3))

class ChatBotGroq:
    def __init__(self, faq_path=FAQ_PATH):
        self.faq = pd.read_csv(faq_path)
        self.vectorizer = TfidfVectorizer()
        self.X = self.vectorizer.fit_transform(self.faq['question'])

    def get_answer(self, user_question):
        """
        Try FAQ match; if none, fallback to Groq LLM.
        """
        uq_clean = clean_text(user_question)
        user_vec = self.vectorizer.transform([uq_clean])
        sim_scores = cosine_similarity(user_vec, self.X)
        best_index = sim_scores.argmax()

        if sim_scores[0][best_index] >= THRESHOLD:
            # FAQ answer
            return self.faq['answer'][best_index]
        else:
            # Fallback to Groq LLM
            return query_groq(user_question)
