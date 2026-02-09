import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
from textblob import TextBlob
from dotenv import load_dotenv
import os
from chatbot.utils import clean_text

load_dotenv()

FAQ_PATH = os.getenv("FAQ_PATH", "data/faq.csv")
THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", 0.3))
LOG_FILE = os.getenv("LOG_FILE", "logs/logs.csv")

class ChatBot:
    def __init__(self, faq_path=FAQ_PATH):
        self.faq = pd.read_csv(faq_path)
        self.vectorizer = TfidfVectorizer()
        self.X = self.vectorizer.fit_transform(self.faq['question'])

    def detect_sentiment(self, text):
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0:
            return "positive"
        elif polarity < 0:
            return "negative"
        else:
            return "neutral"

    def get_answer(self, user_question, threshold=THRESHOLD):
        user_question_clean = clean_text(user_question)
        user_vec = self.vectorizer.transform([user_question_clean])
        sim_scores = cosine_similarity(user_vec, self.X)
        indices = [i for i, score in enumerate(sim_scores[0]) if score >= threshold]

        if not indices:
            # Suggest similar questions
            top_indices = sim_scores[0].argsort()[-3:][::-1]
            suggestions = [self.faq['question'][i] for i in top_indices]
            return f"Sorry, I didn't understand your question. Did you mean: {suggestions}?"
        
        answer = self.faq['answer'][random.choice(indices)]
        self.log_conversation(user_question, answer)
        return answer

    def log_conversation(self, user_question, bot_answer):
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        import csv
        with open(LOG_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([user_question, bot_answer, self.detect_sentiment(user_question)])
