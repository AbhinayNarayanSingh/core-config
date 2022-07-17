from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path("blogs/", PostsListCreateAPIView.as_view(), name="blog"),
    path("blogs/<slug:pk>", PostsRetrieveUpdateDestroyAPIView.as_view(), name="blog")
]