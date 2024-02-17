from django.shortcuts import render

# Create your views here.

def homepage(request):
    # Render the homepage
    return render(request, 'homepage/index.html', context={})
