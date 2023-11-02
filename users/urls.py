from django.urls import path
# from .views import UserRegisterView
from .views import RegisterView

urlpatterns = [
    # path('register/', UserRegisterView.as_view(), name='register'),
    path('register/', RegisterView.as_view(), name='register'),
]
