from django.shortcuts import render
from blog.models import Post

# Create your views here.

def homepage(request):
    """
    A view to return the homepage from :model:`blog.Post`.

    **Context**
    ``top_posts``
        An instance of :model:`blog.Post` to display the top 3 posts.

    **Template:**
    :template:`homepage/index.html`
    """
    post = Post.objects.all()

    top_posts = post.order_by("-view_count")[:3]
    list_of_posts = post.order_by('-view_count')
    list_of_posts1 = list_of_posts[:5]
    list_of_posts2 = list_of_posts[5:10]

    context={
            'top_posts': top_posts,
            "list_of_posts1": list_of_posts1,
            "list_of_posts2": list_of_posts2,
            }
    return render(request, 'homepage/index.html', context)
