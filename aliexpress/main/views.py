from django.shortcuts import render
from .models import *

def homepage(request):
    return render(request, "index.html", {})
