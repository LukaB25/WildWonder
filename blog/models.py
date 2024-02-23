from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, 'Published'), (1, 'Draft'))


# Create your models here.
    

class Post(models.Model):
    """
    Stores the article blog posts and their content.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    location_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    location_description = models.TextField(max_length=500, blank=False)
    main_content_title = models.CharField(max_length=100, blank=True)
    main_content = models.TextField(max_length=1500, blank=False)
    secondary_content = models.TextField(max_length=1500, blank=False)
    longitude = models.FloatField(blank=False)
    latitude = models.FloatField(blank=False)
    view_count = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.location_name} | Written by: {self.author}"


class Comment(models.Model):
    """
    Stores the comments on the blog posts.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    body = models.TextField(max_length=200, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment: {self.body} | Written by: {self.author} | On a post: {self.post.location_name}"


class Vote(models.Model):
    """
    Stores the votes on the blog posts.
    """
    STAR_CHOICES = (
        (1, '1 Star'), 
        (2, '2 Stars'), 
        (3, '3 Stars'), 
        (4, '4 Stars'), 
        (5, '5 Stars'),
        )


    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes')
    voter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='voter')
    user_vote = models.IntegerField(choices=STAR_CHOICES, default=0)
    vote_total = models.FloatField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def voteTotal(self):
        votes = Vote.objects.filter(post=self.post)
        vote_total = votes.aggregate(models.Sum('user_vote')) / votes.count()

        return vote_total

    def __str__(self):
        return f"Vote: {self.user_vote} | On a post: {self.post.location_name} | By: {self.voter}"