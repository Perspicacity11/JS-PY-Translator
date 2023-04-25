# from django.http import HttpResponse
from django.shortcuts import render
import openai, os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)

# Create your views here.
def index(request):
    chatbot_response = None
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input

        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = prompt,
            max_tokens = 256,
            # stop = '.' #update this as this represents the end of the prompt (a full stop in this case)
            temperature = 0.5, #this setting dictates the creativity of the response
        )
        print(response)

        chatbot_response = response['choices'][0]['text']
    return render(request, 'index.html', {'response': chatbot_response})

# I need to provide the logic from logic.py as a third argument to this render (so I'll need to import the logic file)