from django.shortcuts import render
from .data_parser import *
from .models import *

def homepage(request):

    search = request.GET.get('product')
    checked = request.GET.get('freeshipping')

    if search == None:
        print("Hello! Enjoy my intentionally small and slow web scraper.")
        print("I made this just to show that I can do these kinds of things ;)")
    else:
        PageSourceParsing.page_source(search, checked)
        print("Scraping Complete")

    return render(request, "index.html", {})
