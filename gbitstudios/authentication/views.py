from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    response = {}
    return render(request, 'home.html', response)
    #return HttpResponse("<h1>Homepage</h1>")
