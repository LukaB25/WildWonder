from django.urls import path
from ..homepage import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
]