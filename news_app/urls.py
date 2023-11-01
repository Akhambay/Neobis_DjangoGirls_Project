from django.urls import path
from .views import HomeView, NewsDetailView, AddNewsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news-details'),
    path('add_news/', AddNewsView.as_view(), name='add_news')
]
