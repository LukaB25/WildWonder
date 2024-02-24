import datetime
import random
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.utils.text import slugify
from better_profanity import profanity
from .flagged_words import flagged_words
from .forms import CommentForm, VoteForm, ArticleForm
from .models import Post, Comment

# Create your views here.


flagged_words_list = flagged_words
profanity.load_censor_words(flagged_words_list)


def flagged_word_moderator(content):
    """
    Function to moderate the content of the blog posts and comments.
    """
    words = content.split()
    for word in words:
        if profanity.contains_profanity(word):
            return word
    return None


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

    # Pagination
    paginator = Paginator(published_posts, 6)
    page_number = request.GET.get('page') or 1
    article_page_obj = paginator.get_page(page_number)

    # Pass the published posts/articles to the template context
    context = {
        'posts': published_posts,
        'article_page_obj': article_page_obj,
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

    # Pagination
    paginator = Paginator(comments, 3)
    page_number = request.GET.get('page') or 1
    page_obj = paginator.get_page(page_number)

    if request.method == "POST":
        if 'comment_submit' in request.POST:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment_body = request.POST.get('body').lower()
                if flagged_word_moderator(comment_body):
                    comment = comment_form.save(commit=False)
                    comment.author = request.user
                    comment.post = post
                    comment.approved = False
                    comment.save()
                    messages.add_message(request, messages.ERROR,'Comment has been flagged due to inappropriate language. It will be reviewed by the moderator.')
                else:
                    comment = comment_form.save(commit=False)
                    comment.author = request.user
                    comment.post = post
                    comment.save()
                    messages.add_message(request, messages.SUCCESS,'Comment submitted')
                    # Pagination
                    paginator = Paginator(comments, 3)
                    page_number = request.GET.get('page') or 1
                    page_obj = paginator.get_page(page_number)
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

    # Get the total votes for the post
    vote_count = post.votes.all().count()
    # Calculate the sum of all votes for the post and the total vote score
    vote_sum = post.votes.aggregate(Sum('user_vote'))['user_vote__sum'] if vote_count > 0 else 0
    vote_total = round(vote_sum / vote_count, 1) if vote_count > 0 else 0

    # Get the count of approved comments for the post
    comment_count = post.comments.filter(approved=True).count()

    return render(
        request, 
        'blog/article.html', 
        {
            'post': post,
            'page_obj': page_obj,
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
            comment_body = request.POST.get('body').lower()
            if flagged_word_moderator(comment_body):
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.approved = False
                comment.save()
                messages.add_message(request, messages.ERROR,'Comment has been flagged due to inappropriate language. It will be reviewed by the moderator.')
            else:
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
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


def write_article(request):
    """
    view to write a new article
    """
    def fictional_views():
        """
        Function to calculate the fictional views of the article
        """
        return random.randint(300, 1300)
    
    def fictional_rating():
        """
        Function to calculate the fictional rating of the article
        """
        return round(random.randint(10, 50)/10, 1)
    
    def fictional_comments():
        """
        Function to calculate the fictional comments of the article
        """
        return random.randint(1, 300)
    
    
    fictional_view_count = fictional_views()
    fictional_vote_total = fictional_rating()
    fictional_comment_count = fictional_comments()
    fictional_updated_on = datetime.datetime.now()

    if request.method == "POST":
        article_form = ArticleForm(data=request.POST)
        if article_form.is_valid():
            location_name = request.POST.get('location_name')
            location_description = request.POST.get('location_description')
            main_content_title = request.POST.get('main_content_title')
            main_content = request.POST.get('main_content')
            secondary_content = request.POST.get('secondary_content')
            longitude = request.POST.get('longitude')
            latitude = request.POST.get('latitude')

            condensed_article_text = '\n'.join([
                    location_name,
                    location_description,
                    main_content_title,
                    main_content,
                    secondary_content,
                    longitude,
                    latitude
                    ])
            if flagged_word_moderator(condensed_article_text):
                messages.add_message(request, messages.ERROR, 'Article has been flagged due to inappropriate language. It will be reviewed by the moderator.')
                post_instance = article_form.save(commit=False)
                post_instance.status = 2
            else:
                messages.add_message(request, messages.SUCCESS, 'Article submitted!')
                post_instance = article_form.save(commit=False)
                post_instance.status = 0

            slug = slugify(location_name)
            post_instance.location_name = location_name
            post_instance.slug = slug
            post_instance.location_description = location_description
            post_instance.author = request.user
            post_instance.main_content_title = main_content_title
            post_instance.main_content = main_content
            post_instance.secondary_content = secondary_content
            post_instance.longitude = longitude
            post_instance.latitude = latitude
            post_instance.save()
            return HttpResponseRedirect(reverse('article_detail', args=[slug]))    
    else:
        article_form = ArticleForm()

    context = {
        'fictional_view_count': fictional_view_count,
        'fictional_vote_total': fictional_vote_total,
        'fictional_comment_count': fictional_comment_count,
        'fictional_updated_on': fictional_updated_on,
        'article_form': article_form,
    }
    
    print('Article created!')
    return render(request, 'blog/article_create.html', context)

def edit_article(request, slug):
    """
    View to edit an article
    """
    queryset = Post.objects.filter(status=0)
    post = get_object_or_404(queryset, slug=slug)

    if request.method == "POST":
        article_form = ArticleForm(data=request.POST, instance=post)
        if article_form.is_valid() and post.author == request.user:
            location_name = request.POST.get('location_name')
            location_description = request.POST.get('location_description')
            main_content_title = request.POST.get('main_content_title')
            main_content = request.POST.get('main_content')
            secondary_content = request.POST.get('secondary_content')
            longitude = request.POST.get('longitude')
            latitude = request.POST.get('latitude')

            condensed_article_text = '\n'.join([
                    location_name,
                    location_description,
                    main_content_title,
                    main_content,
                    secondary_content,
                    longitude,
                    latitude
                    ])
            if flagged_word_moderator(condensed_article_text):
                messages.add_message(request, messages.ERROR, 'Article has been flagged due to inappropriate language. It will be reviewed by the moderator.')
                post_instance = article_form.save(commit=False)
                post_instance.status = 2
            else:
                messages.add_message(request, messages.SUCCESS, 'Article updated!')
                post_instance = article_form.save(commit=False)
                post_instance.status = 0
            post_instance.location_name = location_name
            post_instance.slug = slug
            post_instance.location_description = location_description
            post_instance.author = request.user
            post_instance.main_content_title = main_content_title
            post_instance.main_content = main_content
            post_instance.secondary_content = secondary_content
            post_instance.longitude = longitude
            post_instance.latitude = latitude
            post_instance.save()
            return redirect('article_detail', slug=post.slug)
        else:
            if not post.author == request.user:
                messages.add_message(request, messages.ERROR, 'You are not authorized to edit this article.')
            return render(request, 'blog/article_edit.html', {'post':post, 'article_form': article_form})
    else:
        article_form = ArticleForm(instance=post)

    return render(request, 'blog/article_edit.html', {'post':post, 'article_form': article_form})

def delete_article(request, slug):
    """
    View to delete an article
    """
    queryset = Post.objects.filter(status=0)
    post = get_object_or_404(queryset, slug=slug)

    if post.author == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Article deleted!')
    elif request.user.is_superuser:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Article deleted by superuser!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own articles!')

    return HttpResponseRedirect(reverse('articles_page'))