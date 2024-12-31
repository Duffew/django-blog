from django.shortcuts import render
# Add an import for HttpResponse from django.http at the top of the file.
from django.http import HttpResponse

# Create your views here.
# add a function to return the text string "Hello, Blog!".
def my_blog(request):
    return HttpResponse("Hello, Blog!")