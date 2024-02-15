from django import forms
from .models import ContactForm, SUBJECTS

class ContactFormMessage(forms.ModelForm):
    """
    A form for users to contact the site owner.
    """
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'subject', 'message']
