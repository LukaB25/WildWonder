from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('location_name', 'author', 'status')
    search_fields = ['title', 'author']
    list_filter = ('status', 'created_on', 'updated_on')
    prepopulated_fields = {'slug': ('location_name',)}
    summernote_fields = ('location_description', 'main_content', 'secondary_content')


# Register your models here.
admin.site.register(Comment)
