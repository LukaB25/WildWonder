from django.urls import path
from . import views

urlpatterns = [
    path('write/', views.write_article, name='write_article'),
    path('<slug:slug>/delete/', views.delete_article, name='delete_article'),
    path('<slug:slug>/edit/', views.edit_article, name='edit_article'),
    path('<slug:slug>/', views.article_detail, name="article_detail"),
    path('<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
    path('', views.articles_page, name='articles_page'),
]
