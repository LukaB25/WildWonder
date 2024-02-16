from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('location_name', 'author', 'status')
    search_fields = ['title', 'author']
    list_filter = ('status', 'created_on', 'updated_on')
    prepopulated_fields = {'slug': ('location_name',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('post', 'author', 'status')
    search_fields = ['post', 'author']
    list_filter = ('status', 'created_on', 'updated_on')
