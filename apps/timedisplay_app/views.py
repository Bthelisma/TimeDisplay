from django.shortcuts import render, HttpResponse, redirect
from time import gmtime
import datetime

def index(request):
    context = {
    "now": datetime.datetime.now()

    }
    return render(request,'timedisplay_app/index.html', context)
