from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(reuqest):
    return HttpResponse("Hello, world. You're at the tododatabase index.")
