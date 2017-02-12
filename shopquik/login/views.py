from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.hashers import make_password
from .models import *
import requests
import json

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
                    list_form = ListForm()
                    return render(request,'shopquik/profile.html/', {
                        'user': user,
                        'list_form':list_form
                    })
                else:
                    # Return an 'invalid login' error message.
                    return HttpResponse("Sign in Error!")
        else:
            signin_form = SignInForm()
            return render(request, 'shopquik/login/signin.html/', {'signin_form':signin_form})
    else:
        signin_form = SignInForm()
    return render(request, "shopquik/signin.html/",{'signin_form':signin_form})

def createList(request):
    if request.method == 'POST':
        if 'list_submit' in request.POST:
            list_form = ListForm(request.POST)
            list_name = request.POST.get('list_name')
            if list_form.is_valid():
                request.session['list_name'] = list_form.data['list_name']
                item_form = ItemForm()
                list_form.save()
                return render(request,'shopquik/list.html',{
                    'list_name': list_name,
                    'item_form': item_form
                })
            else:
                list_form = ListForm()
                return render(request, 'shopquik/profile.html/', {'list_form':list_form})
        else:
            list_form = ListForm()
            return render(request,'shopquik/profile.html/', {'list_form':list_form})
    else:
        list_form = ListForm()
    return render(request, "shopquik/profile.html/",{'list_form':list_form})

def addItems(request):
    # list_name = request.POST.get('list_name')
    list_name = request.session['list_name']
    list = List.objects.filter(list_name=list_name)
    if request.method == 'POST':
        if 'item_submit' in request.POST:
            item_form = ItemForm(request.POST)
            if item_form.is_valid():
                i = item_form.save()
                list[0].items.add(i)
                item_form = ItemForm()

                # return HttpResponse("Items saved!")
                return render(request,'shopquik/list.html/',{'item_form':item_form,'list_name':list_name,'lists':list})
            else:
                item_form = ItemForm()
                return render(request,'shopquik/list.html/',{'item_form':item_form,'list_name':list_name,'lists':list})
        else:

            item_form = ItemForm()
            return render(request,'shopquik/list.html/',{'item_form':item_form,'list_name':list_name,'lists':list})
    else:
        item_form = ItemForm()
    return render(request,'shopquik/list.html/',{'item_form':item_form,'list_name':list_name,'lists':list})

def stores(request):
    list_name = request.session['list_name']
    if request.POST:
        address = request.POST.get("address", "")
        requestString = "https://maps.googleapis.com/maps/api/geocode/json?address="+ str(address) +"&key=AIzaSyAwpVMPCRmLfoa7CxGQr4SrmmkwPm4iiSE"
        locdata = requests.get(requestString)
        loc = json.loads(locdata.text)['results'][0]['geometry']['location']
        location = str(loc['lat']) + ',' + str(loc['lng'])
        data = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+ str(location) +"&radius=5000&keyword=Stater&key=AIzaSyC5Ygtct3M5odZ_iu45po0Rby9I3VEpLZc")
        stores = json.loads(data.text)['results']
    else:
        stores = ""
    return render(request, 'shopquik/store.html/', {
        "store_list": stores,
        "list": list,
        "list_name":list_name
    })

def map(request):
    list_name = request.session['list_name']