from django.shortcuts import render
from .data_parser import *
from .csv_handling import *
from .models import *

csvfilename = ['tobacco']

def homepage(request):

    search = request.GET.get('product')
    checked = request.GET.get('freeshipping')
    #download = request.GET.get('download')

    if search == None:
        print("Hello! Enjoy my intentionally small and slow web scraper.")
        print("I made this just to show that I can do these kinds of things ;)")
    else:
        PageSourceParsing.page_source(search, checked)
        print("Scraping Complete")

    if len(csvfilename) == 0 or search == csvfilename[-1]:
        CSV_Handling.download_csv(csvfilename)
        print('Download Complete')
    else:
        print('No search was recorded')

    csvfilename.append(search)



    return render(request, "index.html", {})
