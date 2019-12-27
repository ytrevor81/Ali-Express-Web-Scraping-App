from django.shortcuts import render
from .data_parser import *
from .models import *

def homepage(request):

    search = request.GET.get('product')
    checked = request.GET.get('freeshipping')
    print(search)
    print(checked)


    #PageSourceParsing.page_source(search, checked)



    return render(request, "index.html", {})
