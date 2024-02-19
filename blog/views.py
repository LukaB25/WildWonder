from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .forms import CommentForm
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=0)
    template_name = "blog/articles_page.html"
    paginate_by = 6


def articles_page(request):
    """
    Display a list of published :model:`blog.Post`
    **Context**
    ``posts``
        A queryset of published_posts :model:`blog.Post`
    **Template:**
    :template:`blog/articles_page.html`
    """

    published_posts = Post.objects.filter(status=0)

    # Pass the published posts/articles to the template context
    context = {
        'posts': published_posts,
    }

    # Render the articles page template with the context
    return render(request, 'blog/articles_page.html', context)

def article_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**
    
    ``post``
        An instance of :model:`blog.Post`.

    **Template:**
    :template:`blog/article.html`
    """
    queryset = Post.objects.filter(status=0)
    post = get_object_or_404(queryset, slug=slug)
    # Increment the view count of the post each time the article is viewed
    post.view_count += 1 # Luka!!! Return to 0 before deployment!!!
    post.save()

    # Get all the comments for the post and display them in descending order
    comments = post.comments.all().order_by("-created_on")

    # Get the count of approved comments for the post
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS,'Comment submitted')
        else:
            messages.add_message(request, messages.ERROR,'Comment not submitted. Please try again.')

    comment_form = CommentForm()

    return render(
        request, 
        'blog/article.html', 
        {
            'post': post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )