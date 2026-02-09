import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_MODEL = os.getenv("GROQ_MODEL", "mixtral-8x7b-32768")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def query_groq(prompt: str) -> str:
    """
    Call Groq chat completions API to get an LLM generated response.
    """
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        model=GROQ_MODEL,
        temperature=0.6,
    )
    # Return text from first choice
    return response.choices[0].message.content
