from django.shortcuts import render
from django.contrib import messages
from .models import ContactAboutSection
from .forms import ContactFormMessage

# Create your views here.

def contact(request):
    """
    Renders the contact page with the ContactAboutSection and ContactMessageForm.
    """
    contact_form = ContactFormMessage()
    if request.method == 'POST':
        contact_form = ContactFormMessage(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            
            messages.add_message(
                request, messages.SUCCESS, 'Your message has been received. Thank you for getting in touch with us!'
            )
        else:
            messages.add_message(
                request, messages.ERROR, 'There was an error with your form. Please try again.'
            )
    
    contact = ContactAboutSection.objects.all().order_by('-updated_on').first()

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'contact_form': contact_form,
        }
    )