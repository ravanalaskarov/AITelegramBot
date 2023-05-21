#https://medium.com/geekculture/a-simple-guide-to-chatgpt-api-with-python-c147985ae28

import openai
openai.api_key = 'OpenAI_API_KEY'

#Place your initial data in the contect filed. Role has to be system in this case
messages = [
    {
    "role": "system",
    "content": "You are the customer service of company called 'The Nirvana'. We provide AI based customer service for the companies."
    }
  ]


def askGPT(message: str) -> str:
    try:
      messages.append({"role": "user", "content": message})

      completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
      )

      chat_response = completion.choices[0].message.content
      
      #Add message to the chat history
      messages.append({"role": "assistant", "content": chat_response})
      return chat_response
    except:
       return "OPENAI API Error"

    