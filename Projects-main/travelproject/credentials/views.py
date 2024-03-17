from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method == 'POST':
        un = request.POST['username']
        fn = request.POST['First_name']
        ln = request.POST['last_name']
        email = request.POST['email']
        pa = request.POST['password']
        cp = request.POST['password1']

        if pa == cp:
            if User.objects.filter(username=un).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email Taken")
                return  redirect('register')
            else:
                us = User.objects.create_user(username=un,password=pa,first_name=fn,last_name=ln,email=email)
                us.save();
                return redirect('login')
                print("user created")
        else:
            messages.info(request, "password not matching conform password")
            return redirect('register')

        return  redirect('/')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        un=request.POST['username']
        pa=request.POST['password']
        us= auth.authenticate(username=un, password=pa)

        if us is not None:
            auth.login(request, us)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')

    return render(request, 'log.html')


def logout(request):
    auth.logout(request)
    return redirect("/")