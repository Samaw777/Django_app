from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'nflpredictor/index.html')

def predictions(request):
    return render(request, 'nflpredictor/predictions.html')
def 