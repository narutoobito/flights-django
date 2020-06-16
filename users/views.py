from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:lin'))
    return render(request,"users/index.html")

def lin(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('users:index'), {"user":user})
        return render(request,"users/login.html", {"message":"wrong credentials"})
    else:
        return render(request,"users/login.html")

def lout(request,user):
    logout(request)
    return render(request,"users/logout.html",{"user": user})
