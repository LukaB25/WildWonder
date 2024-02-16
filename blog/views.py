from django.shortcuts import render
from .models import Post

# Create your views here.

def articles_page(request):
    # Retrieve all published posts/articles
    # Article page is name Wonders on the site
    published_posts = Post.objects.filter(status=0)

    # Pass the published posts/articles to the template context
    context = {
        'posts': published_posts,
    }

    # Render the articles page template with the context
    return render(request, 'blog/articles_page.html', context)
