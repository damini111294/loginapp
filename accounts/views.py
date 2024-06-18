from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
import re

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def signupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("your password and confirm password are not match")
        else:


           my_user=User.objects.create_user(uname,email,pass1)
           my_user.save()
           return redirect('login')

       
    return render (request,'signup.html')

def loginPage(request):
    if request.method=='POST':
         username=request.POST.get('username')
         pass1=request.POST.get('pass')
         user=authenticate(request,username=username,password=pass1)
         if user is not None:
             login(request,user)
             return redirect('home')
         else:
             return HttpResponse("username or password is incorrect!!!")
    return render (request,'login.html')
def logoutpage(request):
    logout(request)
    # return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Example validation (you should customize this)
        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long')
            return render(request, 'login.html')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
        



    # def login_view(request):
    #   if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')

    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('home')  # Redirect to the home page after successful login
    #     else:
    #         messages.error(request, 'Invalid username or password')
    #         return render(request, 'login.html')
    

    return render(request, 'login.html')
