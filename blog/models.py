from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, 'Published'), (1, 'Draft'), (2, 'Deleted'))

# Create your models here.
class Post(models.Model):
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
