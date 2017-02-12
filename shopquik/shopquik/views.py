from django.shortcuts import render
from django.contrib import auth
import requests
import json

def homepage(request):
    return render(request,'shopquik/homepage.html/')

def logout(request):
    auth.logout(request)
    return render(request, "shopquik/homepage.html")
# def stores(request):
#     list_name = request.session['list_name']
#     if request.POST:
#         if(request.POST.get("address", "")):
#             address = request.POST.get("address", "")
#             locdata = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+ str(address) +"&key=AIzaSyAwpVMPCRmLfoa7CxGQr4SrmmkwPm4iiSE")
#             loc = json.loads(locdata.text)['results'][0]['geometry']['location']
#             location = str(loc['lat']) + ',' + str(loc['lng'])
#             data = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+ str(location) +"&radius=5000&keyword=Stater&key=AIzaSyC5Ygtct3M5odZ_iu45po0Rby9I3VEpLZc")
#             stores = json.loads(data.text)['results']
#     else:
#         stores = ""
#     # list = List.objects.filter(list_name=list_name)
#     return render(request, 'shopquik/store.html/', {
#         "store_list": stores,
#         "list": list
#     })

def list(request):
    list = List.object
    return render(request, 'shopquik/list.html/', {
        "list": list
    })