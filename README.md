# Mini FAQ Chatbot 🤖

A **simple FAQ chatbot** capable of answering frequently asked questions from a CSV dataset.  
The project includes a **console version** and a **Streamlit web interface**, with conversation history management and environment variable configuration via `.env`.

---

## **Features**

- Automatic responses to frequently asked questions (FAQ)  
- **Console** and **Streamlit web interface**  
- Conversation history tracking  
- Support for multiple questions in a single input (separated by `;`)  
- Handles unknown questions with a default message  
- Configurable via `.env`:
  - CSV dataset path (`FAQ_PATH`)
  - Similarity threshold (`SIMILARITY_THRESHOLD`)
- Modular code structure (`core.py`, `utils.py`, `session.py`)

---

## **Screenshot**


---

## **Installation**

1. Clone the repository

```bash
git clone https://github.com/YourUsername/mini-faq-chatbot.git
cd mini-faq-chatbot
