from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class NewsDetailView(DetailView):
    model = Post
    template_name = 'news_details.html'


class AddNewsView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_news.html'
    # fields = '__all__'
