from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.article_detail, name="article_detail"),
    path('<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
    path('', views.articles_page, name='articles_page'),
]
