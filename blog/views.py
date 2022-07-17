from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext, gettext_lazy as _

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializer import *

app_name = 'blog'


class PostsListCreateAPIView(ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class PostsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    
