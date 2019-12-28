from django.http import HttpResponse
from django.shortcuts import render, redirect
from .data_parser import *
from .csv_handling import *
from .models import *
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm


csvfilename = []

def homepage(request):
    search = request.GET.get('product')
    checked = request.GET.get('freeshipping')

    if request.method=="POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("homepage")
            else:
                print("INVALID")

    form = AuthenticationForm


    if search == None:
        print("Hello! Enjoy my intentionally small and slow web scraper.")
        print("I made this just to show that I can do these kinds of things ;)")
    else:
        PageSourceParsing.page_source(search, checked)
        csvfilename.append(search)
        print("Scraping Complete")

    if len(csvfilename) == 0:
        filename = None
    else:
        filename = csvfilename[-1]

    return render(request, "homepage.html", {"form": form, "filename": filename})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = RegisterForm
    return render(request, "register.html", {"form": form})

def logout_request(request):
    logout(request)
    return redirect("homepage")
