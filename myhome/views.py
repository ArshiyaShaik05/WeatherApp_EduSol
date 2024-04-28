from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.

def myhomepage(request):
    #return HttpResponse("<center><h2>This is my HomePage</h2></center>")
    return render(request,'myhome.html')

def weather(request):
    city=request.GET.get('city')
    url="http://api.weatherapi.com/v1/current.json?key=1815a4f7ec4d416cb7c151503241802&q=" +str(city)
    response = requests.get(url)
    json_response=json.loads(response.text)
    temp=json_response['current']['temp_c']
    return HttpResponse("<center><h4>The weather of {} is {}*C</h4>".format(city,temp))