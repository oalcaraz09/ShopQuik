from django.http import HttpResponse
from django.shortcuts import render
import datetime

def homepage(request):
    return render(request,'shopquik/homepage.html/')