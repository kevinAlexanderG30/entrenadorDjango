from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hola", request)

def form(request):
    return render(request,"form.html")

def inicio(request):
    return render(request, 'index.html')