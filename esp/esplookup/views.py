from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

def index(request):
    return render(request, 'esplookup/index.html',{})

def lookup(request):
    return render(request,'esplookup/lookupform.html', {})

def query(request):
    submitted_job = request.POST.get('jobname',"False")
    action = request.POST.get('action',"False")

    r = requests.post('https://reqres.in/api/users', data = {'name':submitted_job,'job':action})
    

    command = r.text
    return HttpResponse(command)

