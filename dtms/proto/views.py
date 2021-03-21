from django.shortcuts import render

# Create your views here.

def home(request):
    print("hello")
    return render(request, 'host.html')

def index(request):
    print("hell")
    return render(request, 'index.html')