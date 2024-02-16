from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.PostList.as_view(), name="article"),
    path('', views.articles_page, name='articles_page'),
]
