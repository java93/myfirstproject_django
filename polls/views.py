from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello</h1>\
        <p>Hello World from Bekzat</p>")

def index(request):
    return HttpResponse("<h1>Bye</h1>\
        <p>Good Bye from Bekzat</p>")