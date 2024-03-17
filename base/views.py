from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

#rooms  = [
#    {'id':1, 'name':'Room101'},
#    {'id':2, 'name':'Room102'} 
# ] 

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'myproject/home.html',context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}        
    return render(request, 'myproject/room.html',context)

def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        #print(request.POST)
    context = {'form':form}
    return render(request, 'myproject/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk) #get value by pk
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'myproject/room_form.html' ,context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'myproject/delete.html', {'obj':room})

