from django.shortcuts import render
from django.contrib import messages
from .models import ContactAboutSection, ContactForm

# Create your views here.

def contact(request):
    """
    Renders the contact page with the ContactAboutSection and ContactForm.
    """
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            
            messages.add_message(
                request, messages.SUCCESS, 'Your message has been received. Thank you for getting in touch with us!'
            )
    
    contact_about = ContactAboutSection.objects.all().order_by('-updated_on').first()

    return render(
        request,
        'contact/contact.html',
        {
            'contact_about': contact_about,
        }
    )