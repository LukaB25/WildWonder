from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Published'), (1, 'Draft'), (2, 'Flagged'))

# Create your models here.


class Post(models.Model):
    """
    Stores the article blog posts and their content.
    The author field is a foreign key to the User model. It relates each
    article to a specific user.
    The location_name field is used to store the title of the article.
    The slug field is used to create a unique URL for the article.
    The slug is created from the location_name field.
    The location_description field is used to store a brief description of the
    article.
    The main_content_title field is used to store the title of about section
    content. It is optional whether the user will use it.
    The main_content field is used to store the main content of the article.
    The hero_image field is used to store the main image of the article which
    will be displayed in the hero section of the article. It uses Cloudinary
    to store the image. If no image is uploaded, a placeholder image will be
    displayed.
    The secondary_content field is used to store the secondary content that
    will be displayed along side a map.
    The longitude and latitude fields are used to store the coordinates of the
    location. They are being read and used by the map on the article page.
    The view_count field is used to store the number of times the article has
    been viewed.
    The comment_count field is used to store the number of comments on the
    article.
    The created_on field is used to store the date and time the article was
    written.
    The updated_on field is used to store the date and time the article was
    last updated.
    The approved field is used to store whether the article is approved or not.
    Approved articles are displayed on the website.
    The status field is used to store the current status of the article.
    Default status is Published which are articles displayed on the site, Draft
    and flagged articles are not displayed on the website. Only admin can
    create drafts and flagged articles are created automatically when a one of
    flagged words inside the flagged_words list is found in the article.
    The post_code_type is used to store whether the article contains code or
    not.
    Only admin can create articles with code. And the coded article needs to be
    confirmed inside the admin panel, by ticking the post_code_type checkbox.
    Otherwise the article will be displayed as regular article.

    Required fields are: location_name, location_description, main_content,
    secondary_content, longitude, latitude.
    Auto fields are:  author, slug(created from location_name), view_count,
    comment_count, created_on, updated_on, approved(default is True),
    status(default is Published), post_code_type(default is False).
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="blog_posts")
    location_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    location_description = models.TextField(max_length=500, blank=False)
    main_content_title = models.CharField(max_length=100, blank=True)
    main_content = models.TextField(max_length=1500, blank=False)
    hero_image = CloudinaryField('image', default='placeholder')
    secondary_content = models.TextField(max_length=1500, blank=False)
    longitude = models.FloatField(blank=False)
    latitude = models.FloatField(blank=False)
    view_count = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=True)
    status = models.IntegerField(choices=STATUS, default=0)
    post_code_type = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.location_name} | Written by: {self.author}"


class Comment(models.Model):
    """
    Stores the comments on the blog posts.

    The post field is a foreign key to the Post model.
    It relates each comment to a specific post.
    The author field is a foreign key to the User model.
    It relates each comment to a specific user.
    The body field is used to store the content of the comment.
    The created_on field is used to store the date and time the comment was
    made.
    The approved field is used to store whether the comment is approved or not.
    Approved comments are displayed on the website. Comments are approved
    initially unless they contain flagged word.
    Each comment is ran through the flagged_word_moderator which checks if the
    comment contains any of the flagged words. If it does, the comment is
    automatically flagged and not displayed on the website. It is only visible
    to the user that wrote it and the admin.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='commenter')
    body = models.TextField(max_length=200, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        comment_string = f"Comment: {self.body}"
        author_string = f"Written by: {self.author}"
        post_string = f"On a post: {self.post.location_name}"
        return f"{comment_string} | {author_string} | {post_string}"


class Vote(models.Model):
    """
    Stores the votes on the blog posts.

    The post field is a foreign key to the Post model. It relates each vote
    to a post.
    The voter field is a foreign key to the User model. It relates each vote
    to a specific user.
    The user_vote field is used to store the value of the vote.
    The vote_total field is used to store the total value of the votes.
    The created_on field is used to store the date and time the vote was made.

    Required fields are: post, voter, user_vote.
    Auto fields are: vote_total, created_on.
    """
    STAR_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
        )

    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='votes')
    voter = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='voter')
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
        vote_string = f"Vote: {self.user_vote}"
        post_string = f"On a post: {self.post.location_name}"
        voter_string = f"By: {self.voter}"
        return f"{vote_string} | {post_string} | {voter_string}"


class Image(models.Model):
    """
    Stores the images on the blog posts.

    The image field is used to store the image of the article.
    The post field is a foreign key to the Post model. It relates each image
    to a specific post.
    The author field is a foreign key to the User model. It relates each image
    to a specific user.
    The created_on field is used to store the date and time the image was
    uploaded.

    Required fields are: image, post, author.
    Auto fields are: created_on.
    """
    image = CloudinaryField('image', blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='images')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='image_author')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
