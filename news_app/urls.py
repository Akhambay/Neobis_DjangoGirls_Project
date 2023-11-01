from django.urls import path
from .views import HomeView, NewsDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news-details'),
]
