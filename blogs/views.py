from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog, Post
# Create your views here.
class BlogList(ListView):
    model = Blog

class BlogDetail(DetailView):
    model = Blog

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post