from django.shortcuts import render,redirect,HttpResponseRedirect
# from django.core.urlresolvers import reverse

from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    # print(request.user)
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')

            login(request,user)
            messages.success(request,f'New account created:{username}')
            return redirect('homepage')
        else:

            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return render(request,'accounts/register.html',{'form':form})

    form=SignUpForm()
    return render(request,'accounts/register.html',{'form':form})
def signin(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            # print(user)
            # user = User.objects.filter(Q(username=username) | Q(email=username))
            if user is not None:
                login(request,user)
                print(request.user)
                # print(messages.info(request,f'You are logged in as {username}'))
                return redirect('/')
            else:
                messages.error(request,'Invalid email or password')
        else:
            messages.error(request, "Invalid username or password.")
    form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})
def logout_view(request):
    logout(request)
    messages.info(request," You have succesfully logged out")
    response = redirect('/')
    return response

