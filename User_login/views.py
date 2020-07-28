from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import auth
# Create your views here.


def show_register(request):
    if request.method == 'POST':
        fn = request.POST['fn']
        ln = request.POST['ln']
        em = request.POST['em']
        un = request.POST['un']
        pw = request.POST['pw']
        user = User.objects.create_user(first_name=fn, last_name=ln, email=em, username=un, password=pw)
        user.save()
        return HttpResponse('<script>alert("User Registered !")</script>')
        return redirect('/users/login')
    return render(request,'registration.html')

def show_login(request):
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        user = auth.authenticate(username=un, password=pw)
        if user is not None:
            auth.login(request, user)
            # return redirect('../users/login')
            return redirect('/home')
        else:
            return HttpResponse('<script>alert("Wrong id or password")</script>')
    return render(request, 'login.html')


@login_required()
def show_dashboard(request):
    # return render(request,'dashboard.html')
    return render(request, 'dashboard.html')


def do_logout(request):
    auth.logout(request)
    return redirect('../../')

