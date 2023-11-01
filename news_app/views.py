from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class NewsDetailView(DetailView):
    model = Post
    template_name = 'news_details.html'


class AddNewsView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_news.html'
    # fields = '__all__'


class UpdateNewsView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_news.html'
    # fields = ['title', 'title_tag', 'body']


class DeleteNewsView(DeleteView):
    model = Post
    template_name = 'delete_news.html'
    success_url = reverse_lazy('home')
