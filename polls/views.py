from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("You're on main page")

def detail(request,post_id):
    return HttpResponse("You're looking at post %s."% post_id)

def create(request):
    return HttpResponse("You're creating new post")