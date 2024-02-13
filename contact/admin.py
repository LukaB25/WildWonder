from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ContactAboutSection, ContactForm


@admin.register(ContactAboutSection)
class ContactAboutSectionAdmin(admin.ModelAdmin):
    list_display = ('hero_title', 'main_title')
    search_fields = ['hero_title', 'main_title']
    summernote_fields = ('hero_message', 'main_message')

@admin.register(ContactForm)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_on', 'read')
    search_fields = ['name', 'email', 'subject']
    list_filter = ('subject', 'created_on', 'read')
