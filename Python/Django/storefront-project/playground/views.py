from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calc():
    return 1

def say_hello(request):
    x = calc()
    y = 2
    return render(request, 'hello.html', {'name': 'Deepak'})
