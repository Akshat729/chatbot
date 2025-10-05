
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

history = []

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chatbot(prompt):
    history.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=history
    )

    reply = response.choices[0].message.content

    history.append({"role": "assistant", "content": reply})

    return reply

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("Bot: ", chatbot(user_input))