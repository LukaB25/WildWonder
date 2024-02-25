from django.shortcuts import render
from django.contrib import messages
from .models import ContactAboutSection
from .forms import ContactFormMessage

# Create your views here.

def contact(request):
    """
    A view to return the contact page from :model:`contact.ContactAboutSection` and :model:`contact.ContactFormMessage`.

    **Context**
    ``contact``
        An instance of :model:`contact.ContactAboutSection` to display the contact information.

    ``contact_form``
        An instance of :model:`contact.ContactFormMessage` to display the contact form.

    **Template:**
    :template:`contact/contact.html`
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