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

st.title("Synapse GPT")
st.write("El mejor chatbot de la historia basado en GPT-3.5")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

st.session_state["messages"] = [{"role": "assistant", "content": "Hola, en que puedo ayudarte?"}]
for message in st.session_state["messages"]:
   st.chat_message(message["role"]).write(message["content"])




if user_input := st.chat_input():
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)
    response = op.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= st.session_state["messages"]
    )
    responseMessage = response['choices'][0]['message']['content']
    st.session_state["messages"].append({"role": "assistant", "content": responseMessage})
    st.chat_message("assistant").write(responseMessage)


