import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5=turbo",
        messages=[{"role":"user", "content":prompt}],
    )
    return response['choices'][0]['message']['content']
def main():
    print("Welcome to pyhton chatgpt ! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Bye!")
            break
        answer = chat_with_gpt(user_input)
        print(f"Bot: {answer}")

if __name__ == "__main__":
    main()        
