from django.shortcuts import render
from django.http import HttpResponse

from .models import Route

def index(request):
    return HttpResponse("Testing")

def detail(request, route_name):
    return HttpResponse("Route name: %s" % route_name)

