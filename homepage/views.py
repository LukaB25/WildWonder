from django.shortcuts import render
from blog.models import Post, Vote

# Create your views here.

def homepage(request):
    # Render the homepage
    return render(request, 'homepage/index.html', context={})
