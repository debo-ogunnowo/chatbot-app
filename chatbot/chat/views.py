from django.shortcuts import render
from dotenv import load_dotenv
from groq import Groq
import os
from django.http import JsonResponse
from .models import Chat

def index(request):
  return render(request, 'index.html')

load_dotenv()
api_key = os.getenv('key')

client = Groq(api_key=api_key)
def generate_chatbot_response(message):
  completion = client.chat.completions.create(
      model="openai/gpt-oss-20b",
      messages=[
        {
          "role": "user",
          "content": message
        }
      ],
      temperature=1,
      max_completion_tokens=8192,
      top_p=1,
      reasoning_effort="medium",
      stream=False,
      stop=None
  )
  return completion.choices[0].message.content

def response(request):
  if request.method == 'POST':
    message = request.POST.get('message')
    chatbot_response = generate_chatbot_response(message)
    new_chat = Chat(message=message, response=chatbot_response)
    new_chat.save()
    return JsonResponse({'response': chatbot_response})