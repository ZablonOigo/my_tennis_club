from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

def sign_in(request):
    if request.method =='GET':
        if request.user.is_authenticated:
            return redirect('members:index')
        form=LoginForm()
        context={'form':form}
        return render(request,'user/login.html',context)
    elif request.method =='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request, username=username, password=password)
            if user:
                login(request,user)
                messages.success(request,f'{username.title()}, Welcome back')
                return redirect('members:index')
            

    else:
        form=LoginForm()
        context = {'form': form}
        messages.error(request,'Invalid username or password')
        return render(request,'user/login.html',context)    

def sign_out(request):
    logout(request)
    messages.success(request,'You have logged out')
    return redirect ('user:login')


def register(request):
    if request.method =='GET':
        form=RegisterForm()
        context={'form':form}
        return render(request, 'user/register.html',context)
    elif request.method =='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            context={'form':form}
            user.save()
            messages.success(request,'You have signed up successfully')
            login(request,user)
            return redirect('members:index')
        else:
         return render(request,'user/register.html',context)
    