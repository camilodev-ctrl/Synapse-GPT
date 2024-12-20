import openai as op
from dotenv import load_dotenv
import os 
import streamlit as st

load_dotenv()

# op.api_key= os.getenv("OPENAI_API_KEY")
# messages = []
# while True:
#     user_input = input("you: ")
#     if user_input == "0":
#         break

# messages.append({"role": "user", "content": user_input})

# response = op.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=messages
# )
# responseMessage = response['choices'][0]['message']['content']

# messages.append({"role": "assistant", "content": responseMessage}) 

# print("Bot: " + responseMessage)

