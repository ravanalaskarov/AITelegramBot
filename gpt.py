#https://medium.com/geekculture/a-simple-guide-to-chatgpt-api-with-python-c147985ae28

from collections import defaultdict
import openai
openai.api_key = 'OpenAI_API_KEY'
from telegram import Update
#Place your initial data in the contect filed. Role has to be system in this case
messages = [
    {
    "role": "system",
    "content": "You are the customer service of company called 'The Nirvana'. We provide AI based customer service for the companies."
    }
  ]

chat_history = defaultdict(
   lambda: [
    {
    "role": "system",
    "content": "You are the customer service of company called 'The Nirvana'. We provide AI based customer service for the companies."
    }
])


def askGPT(update: Update) -> str:
    try:
      message = update.message.text
      user_history = chat_history[update.effective_user.id]
      
      user_history.append({"role": "user", "content": message})
      
      messages = [{"role": "user", "content": message} for message in user_history]


      completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
      )

      chat_response = completion.choices[0].message.content
      
      #Add message to the chat history
      user_history.append({"role": "assistant", "content": chat_response})
      return chat_response
    except:
       return "OPENAI API Error"

  
