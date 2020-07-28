from django.shortcuts import render
from Rooms.models import room

# Create your views here.
def show_room(request):
    return render(request,'rooms.html')

def show_new(request):
    return render(request,'newrooms.html')

def show_room(request):
    ro=room.objects.all()
    return render(request,'rooms.html',{'ro':ro})
