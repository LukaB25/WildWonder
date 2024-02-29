from django.db import models
from django.contrib.auth.models import User

# Create your models here.

SUBJECTS = (
    (0, 'General Inquiry'),
    (1, 'Report a Bug'),
    (2, 'Feature Request'),
    (3, 'Special Request'),
    (4, 'Other'))


class ContactAboutSection(models.Model):
    """
    Stores the content for the contact page..
    The hero_title and hero_message fields are used to display content inside
    the hero section jumbotron.
    The main_title and main_message fields are used to display content inside
    the about section.

    Required fields are: hero_title, hero_message, main_title, main_message.
    Auto fields are: updated_on.
    """
    hero_title = models.CharField(max_length=100, blank=False)
    hero_message = models.TextField(max_length=600, blank=False)
    main_title = models.CharField(max_length=100, blank=False)
    main_message = models.TextField(max_length=1750, blank=False)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hero_title} | {self.main_title}"


class ContactForm(models.Model):
    """
    Stores the contact requests and messages from Users.
    The name and email fields are used to track who sent the message.
    The created_on field is used to track when the message was sent.
    The subject field is used to track the type of message.
    The read and responded fields are boolean fields that default to False.
    They are used to track the status of the message inside the Admin panel.

    Required fields are: name, email, subject, message.
    Auto fields are: created_on, read(default is False), responded(default is
    False).
    """
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    subject = models.IntegerField(choices=SUBJECTS, default=0)
    message = models.TextField(max_length=1000, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    responded = models.BooleanField(default=False)

    def __str__(self):
        subject_string = f"A {self.subject} message"
        name_string = f"From: {self.name}"
        created_string = f"Sent on: {self.created_on}"
        read_string = f"{self.read}"
        responded_string = f"{self.responded}"
        string1 =  f"{subject_string} | {name_string} | {created_string} | "
        string2 = f"{read_string} | {responded_string}"
        return f"{string1}{string2}"
