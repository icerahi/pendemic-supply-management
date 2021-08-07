from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            messages.success(request, 'You have Logged in successfully')
            return redirect('dashboard')
        else:
            messages.success(request, 'Please Enter Correct Username and Password to Login')
            return redirect('login')

    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')