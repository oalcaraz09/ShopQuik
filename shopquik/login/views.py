from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import UserForm, SignInForm
from django.contrib.auth.hashers import make_password
from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# def signin(request):
#     return render(request, "shopquik/signin.html/")

def signup(request):
    if request.method == 'POST':
        if 'user_submit' in request.POST:
            user_form = UserForm(request.POST)

            if user_form.is_valid():

                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                email = request.POST.get('email')
                password = request.POST.get('password')
                user = User(first_name = first_name, last_name = last_name, email = email, username=email)
                user.set_password(password)
                user.save()
                profile = Profile.objects.get(user=user)
                profile.save()
                # sign_up = user_form.save(commit=False)
                # sign_up.password = make_password(user_form.cleaned_data['password'])
                # sign_up.status = 1
                # sign_up.save()
                return HttpResponse("Submitted!")
        else:
            user_form = UserForm()
            return render(request, 'shopquik/login/signup.html/', {'user_form':user_form})
    else:
        user_form = UserForm()
    return render(request, "shopquik/signup.html/",{'user_form':user_form})

def signin(request):
    if request.method == 'POST':
        if 'signin_submit' in request.POST:
            signin_form = SignInForm(request.POST)
            if signin_form.is_valid():
                data = signin_form.cleaned_data
                email = request.POST.get('email')
                password = request.POST.get('password')
                user = authenticate(username =data['email'] , password = data['password'])
                print("MESSAGE: ", email)
                print("MESSAGE: ", password)
                print("MESSAGE: ", authenticate(username =data['email'] , password = data['password']))
                print("MESSAGE: User is - ", user)
                if user is not None:
                    login(request, user)
                    return HttpResponse("Signed In!")
                else:
                    # Return an 'invalid login' error message.
                    return HttpResponse("Sign in Error!")


                # if request.user.is_authenticated:
                #     return HttpResponse("Signed In!")
                # else:
                #     return HttpResponse("Sign in Error!")

        else:
            signin_form = SignInForm()
            return render(request, 'shopquik/login/signin.html/', {'signin_form':signin_form})
    else:
        signin_form = SignInForm()
    return render(request, "shopquik/signin.html/",{'signin_form':signin_form})

