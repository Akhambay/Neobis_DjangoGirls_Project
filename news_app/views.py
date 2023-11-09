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
    template_name = 'add_news.html'
    success_url = "/news/{id}"
    fields = ['title', 'title_tag', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateNewsView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_news.html'
    success_url = "/news/{id}"


class DeleteNewsView(DeleteView):
    model = Post
    template_name = 'delete_news.html'
    success_url = reverse_lazy('home')
