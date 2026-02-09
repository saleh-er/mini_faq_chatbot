# Mini FAQ Chatbot with Groq 🤖

A **smart FAQ chatbot** that answers frequently asked questions from a CSV dataset and uses a **Groq LLM** for generating responses when no FAQ match is found.  
This project includes a **console version** and a **Streamlit web interface** with conversation history and export functionality.

---

## **Features**

- Automatic FAQ responses using **TF-IDF similarity**
- Fallback to **Groq LLM** for unknown questions
- **Console version** and **Streamlit web interface**
- Conversation history tracking with **export to CSV**
- Supports multiple questions per input
- Configuration via `.env`:
  - `FAQ_PATH` : path to CSV dataset
  - `SIMILARITY_THRESHOLD` : threshold for FAQ matching
  - `GROQ_API_KEY` : Groq API key
  - `GROQ_MODEL` : Groq model to use
- Modular code: `core_groq.py`, `llm.py`, `session.py`, `utils.py`

---

## **Demo Screenshot**

**

---

## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/mini-faq-chatbot.git
cd mini-faq-chatbot
