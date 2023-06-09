#https://medium.com/geekculture/a-simple-guide-to-chatgpt-api-with-python-c147985ae28

from collections import defaultdict
import openai
openai.api_key = 'Your API Key'
from telegram import Update

chat_history = defaultdict(
   lambda: [
    {
    "role": "system",
    "content": "You are the customer service of company called 'The Nirvana'. We provide AI based customer service for the companies."
    }
])


def askGPT(update: Update) -> str:
    message = update.message.text
    user_history = chat_history[update.effective_user.id]
    
    user_history.append({"role": "user", "content": message})
    
    completion = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages = user_history,
      max_tokens = 150,
      temperature = 0.5 
    )

    chat_response = completion["choices"][0]["message"]["content"]
    
    #Add message to the chat history
    user_history.append({"role": "assistant", "content": chat_response})
    print(user_history)
    return chat_response

  
