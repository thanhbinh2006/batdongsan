from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get_app1(request):
    return HttpResponse("hello! this is app 1")
def get_app1_1(request):
    return HttpResponse("hello! this is app 1 child 1")