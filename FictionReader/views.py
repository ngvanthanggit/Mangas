from django.shortcuts import render

from accounts import models
from manga import models
from search import models

def home(request):
    context = {}
    return render(request, 'home.html', context)