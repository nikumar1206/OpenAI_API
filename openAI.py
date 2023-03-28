from os import getenv

import openai
from prompt_toolkit import prompt

import config

# Set up OpenAI API credentials
openai.api_key = config.API_KEY
# Define the chat function using chat completions
def chat(messages):
  try:
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages= messages,
  )

  except:
    print("Error:", "I'm sorry, there was an error. Please try again later.")
    return {"content": "I'm sorry, there was an error. Please try again later."}
  return response["choices"][0]["message"]


# Define the chat bot function
def chatbot():
    print("Hello! I'm a chat bot. How can I help you today?")
    messages = [
      {
        "role": "system",
        "content": "You are a helpful chat bot"
      }
    ]
    while True:
        message = prompt("You: ")
        if message.lower() == "exit":
            break
        messages.append({"role": "user", "content": message})
        response = chat(messages)
        messages.append({"role": "assistant", "content": response["content"]})
        print("Assistant:", response["content"])

# # Run the chat bot

chatbot()