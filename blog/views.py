from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def site_blog(request):
    return HttpResponse('<h1>Blog Home</h1>')