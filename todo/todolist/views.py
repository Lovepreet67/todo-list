from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'todolist/index.html')
def add(request):
    return render (request,"todolist/add.html")