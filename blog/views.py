from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .forms import CommentForm, VoteForm
from .models import Post, Comment, Vote

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
    vote_count = post.votes.all().count()
    vote_sum = post.votes.aggregate(Sum('user_vote'))['user_vote__sum'] if vote_count > 0 else 0
    vote_total = round(vote_sum / vote_count, 1) if vote_count > 0 else 0

    # Get the count of approved comments for the post
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        if 'comment_submit' in request.POST:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                messages.add_message(request, messages.SUCCESS,'Comment submitted')
            elif not comment_form.is_valid():
                messages.add_message(request, messages.ERROR,'Comment not submitted. Please try again.')
        elif 'vote_submit' in request.POST:
            vote_form = VoteForm(data=request.POST)
            if vote_form.is_valid():
                vote = vote_form.save(commit=False)
                vote.post = post
                vote.voter = request.user
                vote.user_vote = request.POST.get('user_vote')
                vote.save()
                messages.add_message(request, messages.SUCCESS, 'Vote submitted!')
            elif not vote_form.is_valid():
                messages.add_message(request, messages.ERROR, 'Error submitting vote!')

    comment_form = CommentForm()
    vote_form = VoteForm()

    return render(
        request, 
        'blog/article.html', 
        {
            'post': post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "vote_total": vote_total,
            "vote_form": vote_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=0)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = True
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('article_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=0)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    elif request.user.is_superuser:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted by superuser!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('article_detail', args=[slug]))


# def vote_submit(request, slug):
#     """
#     view to submit votes
#     """

#     if request.method == "POST":
#         queryset = Post.objects.filter(status=0)
#         post = get_object_or_404(queryset, slug=slug)
#         vote_form = VoteForm(data=request.POST)

#         if vote_form.is_valid():
#             vote = vote_form.save(commit=False)
#             vote.post = post
#             vote.voter = request.user
#             vote.save()
#             messages.add_message(request, messages.SUCCESS, 'Vote submitted!')
#         else:
#             messages.add_message(request, messages.ERROR, 'Error submitting vote!')

#     return HttpResponseRedirect(reverse('article_detail', args=[slug]))