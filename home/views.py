

# Create your views here.
from django.shortcuts import render

# Create your views here.


def show_home(request):
    return render(request, 'home.html')