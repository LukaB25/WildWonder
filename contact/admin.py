from django.contrib import admin
from .models import ContactAboutSection, ContactForm


@admin.register(ContactAboutSection)
class ContactAboutSectionAdmin(admin.ModelAdmin):
    list_display = ('hero_title', 'main_title')
    search_fields = ['hero_title', 'main_title']


@admin.register(ContactForm)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_on',
                    'read', 'responded')
    search_fields = ['name', 'email', 'subject']
    list_filter = ('subject', 'created_on', 'read')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_on')
