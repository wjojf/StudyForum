from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, "name": "Let's Learn python!"},
    {'id': 2, "name": "Flutter let's go!"},
    {'id': 3, "name": "PHP Sucks!"},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    
    room = None 
    
    for x in rooms:
        if x['id'] == int(pk):
            room = x 
    
    context = {'room': room}
    
    return render(request, 'base/room.html', context)
