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
    
    output = r.text
    command = r.json()['name'] + " ==>  " + r.json()['job']
    
    return render(request, 'esplookup/output.html',{ 'output': output , 'command':command,})

