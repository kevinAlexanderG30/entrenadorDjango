from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

rooms = [
    {'id': 1, 'name': 'Aprendiendo Django'},
    {'id': 2, 'name': 'Aprendiendo js'},
    {'id': 3, 'name': 'Aprendiendo ORM'},
    {'id': 4, 'name': 'Aprendiendo CSS'},
    
]

# Que son las querySet

def index(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request,"index.html", context)

def room(request, pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == pk:
    #         room = i
    # context = {'room': room}
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request,"room.html", context)

def inicio(request):
    return render(request, 'index.html')
