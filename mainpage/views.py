from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

# I need to provide the logic from logic.py as a third argument to this render (so I'll need to import the logic file)