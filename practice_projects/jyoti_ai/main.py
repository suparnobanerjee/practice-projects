import openai
import os
from colorama import init, Fore

init(autoreset=True)

openai.api_key = os.environ.get('OPENAI_API_KEY')

def ask_jyoti():
  print(Fore.LIGHTBLUE_EX+"\nHey I'm Jyoti, your AI personal assistant. How can I help you? ")
  query = input()

  while True:

    completion = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
        {"role": "system", "content": "You are Jyoti, a personal AI assistant. Respond to queries from your creator, Suparno, with concise, clear, and optimal answers. Provide examples only if it's necessary."},
        {"role": "user", "content": query}
      ],
      max_tokens=100
    )
    print(Fore.LIGHTGREEN_EX+"\n"+completion.choices[0].message.content+"\n")
    print(Fore.RED+"Jyoti is waiting for your response... (type 'n' to exit)")
    query=input()
    if query.lower()=='n':
      break

if __name__ == "__main__":
    ask_jyoti()



