# from django.http import HttpResponse
from django.shortcuts import render
import openai, os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)
def index(request):
    chatbot_response = None
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = f"""Please translate this JavaScript code into Python, and ensure that the response is formatted as 
        code with appropriate indentation: {user_input}"""

        # Can I write a conditional version of this prompt, which first detects if the input code is JS or PY,
        # and then translates into the other with needing an additional prompt?
        # That or I can have a tickbox in the view for JS-PY and PY-JS, and the state of that variable determines
        # which prompt is used

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