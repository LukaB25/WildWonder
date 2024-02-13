from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, 'Published'), (1, 'Draft'), (2, 'Deleted'))
COMMENT_STATUS = ((0, 'Published'), (1, 'Deleted'))
STAR_CHOICES = ((1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars'),)


# Create your models here.
class Post(models.Model):
    """
    Stores the article blog posts and their content.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    location_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    location_description = models.TextField(max_length=500, blank=True)
    main_content = models.TextField(max_length=1500, blank=True)
    secondary_content = models.TextField(max_length=1500, blank=True)
    longitude = models.FloatField(blank=False)
    latitude = models.FloatField(blank=False)
    view_count = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0)
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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=200, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=True)
    status = models.IntegerField(choices=COMMENT_STATUS, default=0)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment: {self.body} | Written by: {self.author} | On a post: {self.post.location_name}"


class Country(models.Model):
    """
    Stores the country information for the blog posts.
    """
    name = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Vote(models.Model):
    """
    Stores the votes on the blog posts.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes')
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=STAR_CHOICES, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Vote: {self.rating} | On a post: {self.post.location_name} | By: {self.voter}"