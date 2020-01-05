from django.http import HttpResponse
from django.shortcuts import render, redirect
from .data_parser import *
from .csv_handling import *
from .db_handling import *
from .models import *
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm


csvfilename = []    #to store the most recent query, so that the user can download the csv file without being logged in---THIS IS NOT DESIGNED FOR MORE THAN ONE USER AT A TIME!!!! in order to scale this project, this code has to be seriously revised
checked_history = []    #to store if the recent query checked "True" for free shipping


def homepage(request):
    '''Variety of functions are occuring here: Login, web scraping, and when the user is
    verified the email and save data functions are operational'''

    #All GET requests from the homepage
    search = request.GET.get('product')
    amount_string = request.GET.get('amount')
    checked = request.GET.get('freeshipping')
    history_download = request.GET.get('download-query')
    history_delete = request.GET.get('delete-query')
    email_csv = CSV_Handling.boolean_convert(request.GET.get('email-csv'))  #the boolean_convert() method converts the GET request into a boolean value
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
                return redirect("homepage")     #redirects the user to the homepage again; like refreshing the page
            else:
                print("INVALID")

    #Form for User Login
    form = AuthenticationForm

    #Web Scraping function---no need for user verification
    if amount_string != None:
        amount = int(amount_string)     #converts the slider amount into an integer
    else:
        print('amount = None')

    if search == None:
        print('search = None')
    elif search == "":      #ensures the program doesn't crash if the user submits the form without typing in a product name or category
        print('nothing happened')
        csvfilename.clear()     #clears the most recent file name, in case of any unexpected errors
    else:
        PageSourceParsing.page_source(search, amount, checked)  #executes the webscraping functionality
        PageSourceParsing.list_refresh(csvfilename, search)     #ensures the most recent query is in the csvfilename list
        CSV_Handling.csv_file_limit(search)     #Limits the number of csv files in the directory to 5

    #Stores the most recent search, so the user can download or email the .csv file.
    if len(csvfilename) == 0:
        filename = None
    else:
        filename = csvfilename[-1]

    #If the free shipping option is checked, this stores 'True' in the boolean list
    if checked != None:
        PageSourceParsing.list_refresh(checked_history, True)
    else:
        PageSourceParsing.list_refresh(checked_history, False)

    #Email CSV function
    if email_csv == True:
        if request.user.is_authenticated:
            email = request.user.email
            if filename == None:
                print('Do a search or click a past search')
            else:
                CSV_Handling.email_csv_file(filename, email)
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
                CSV_Handling.csv_to_db(filename, username, checked_history[-1])
        else:
            print("SIGN IN OR REGISTER")
    else:
        print("save_csv = {}".format(save_csv))

    #User History Functionality: Make csv from history and Delete
    if request.user.is_authenticated:
        username = request.user.username
        queries = AliSubmission.objects.filter(User=username)[:6]
        print(queries)
        if history_download != None:
            string_tuple = history_download.partition("---")    #the GET request comes in 'query---tableID'. here we separate those from each other
            filename = string_tuple[0]
            id = string_tuple[2]
            CSV_Handling.history_to_csv(username, id)   #this converts the db data from the past query to a csv file
            csvfilename.append(filename)    #this query is put in this list to givbe access to the csv file
        else:
            print('history download = None')
        if history_delete != None:
            DB_Handling.delete_from_db(username, history_delete)    #deletes the past query from the database
        else:
            print('history delete = None')
    else:
        queries = None

    #In case the query has whitespace, this is to ensure it matches with stored csv files that were processed with whitespace
    if filename != None:
        html_filename = filename.replace(" ", "_")
    else:
        html_filename = filename

    return render(request, "homepage.html", {"form": form, "filename": html_filename, "queries": queries, "email": email_csv,
                                             "save": save_csv, "search":search, "history_csv": history_download })

def register(request):
    '''Registers new users using Django forms'''

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    login_form = AuthenticationForm
    register_form = RegisterForm
    return render(request, "register.html", {"register_form": register_form, "form": login_form})

def logout_request(request):
    '''Logs out users and directs them back to the homepage'''
    logout(request)
    return redirect("homepage")
