from django.shortcuts import render
from . import rftxt


def home(request):
    data = rftxt.readunplogs()
    return render(request, 'host.html', {"datalist": data})


def index(request):
    data = rftxt.readlogs()
    return render(request, 'index.html', {"datalist": data})

def activity(request):
    return render(request, 'activity.html')