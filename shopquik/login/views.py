from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

<<<<<<< HEAD
def signin(request):
    return render(request, "shopquik/signin.html/")

def signup(request):
    return render(request, "shopquik/signup.html/")
=======
>>>>>>> origin/master
