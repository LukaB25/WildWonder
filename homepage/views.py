from django.shortcuts import render
from blog.models import Post

# Create your views here.

def homepage(request):
    # Render the homepage
    post = Post.objects.all()

    top_posts = post.order_by("-view_count")[:3]
    return render(request, 'homepage/index.html', context={'top_posts': top_posts})
