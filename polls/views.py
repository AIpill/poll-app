from django.shortcuts import render
from django.http import HttpResponse

# The first view function return Hello world as Response.
def index(request):
    return HttpResponse("Hello, world!")