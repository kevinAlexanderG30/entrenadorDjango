from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

rooms = [
    {'id': 1, 'name': 'Aprendiendo Django'},
    {'id': 2, 'name': 'Aprendiendo js'},
    {'id': 3, 'name': 'Aprendiendo ORM'},
    {'id': 4, 'name': 'Aprendiendo CSS'},
    
]

def index(request):
    context = {'rooms': rooms}
    return render(request,"index.html", context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == pk:
            room = i
    context = {'room': room}
    return render(request,"room.html", context)

def inicio(request):
    return render(request, 'index.html')
