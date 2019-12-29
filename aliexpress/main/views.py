from django.http import HttpResponse
from django.shortcuts import render, redirect
from .data_parser import *
from .csv_handling import *
from .models import *
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm


csvfilename = ['tobacco']

def homepage(request):
    '''Variety of functions are occuring here: Login, web scraping, and when the user is
    verified the email and save data functions are operational'''

    #All GET requests from the homepage
    search = request.GET.get('product')
    checked = request.GET.get('freeshipping')
    email_csv = CSV_Handling.boolean_convert(request.GET.get('email-csv'))
    save_csv = CSV_Handling.boolean_convert(request.GET.get('save-data'))

    #Account Verification and User Login
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

    #Form for User Login
    form = AuthenticationForm

    #Web Scraping function---no need for user verification
    if search != None:
        PageSourceParsing.page_source(search, checked)
        csvfilename.append(search)
        print("Scraping Complete")
    else:
        print('Message for user')

    #Stores the most recent search, so the user can download or email the .csv file.
    if len(csvfilename) == 0:
        filename = None
    else:
        filename = csvfilename[-1]

    #Email CSV function
    if email_csv == True:
        if request.user.is_authenticated:
            email = request.user.email
            if filename == None:
                print('Do a search or click a past search')
            else:
                CSV_Handling.email_csv_file(filename, email)
                print("Email sent!")
        else:
            print('SIGN IN OR REGISTER')
    else:
        print('email_csv = {}'.format(email_csv))

    #Save CSV Function
    if save_csv == True:
        if request.user.is_authenticated:
            username = request.user.username
            if filename == None:
                print('Do a search or click a past search')
            else:
                CSV_Handling.csv_to_db(filename, username)
                print("Data saved!")
        else:
            print("SIGN IN OR REGISTER")
    else:
        print("save_csv = {}".format(save_csv))
        

    return render(request, "homepage.html", {"form": form, "filename": filename})

def register(request):
    '''Register new users'''

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
