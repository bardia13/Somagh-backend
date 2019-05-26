from django.urls import path, include
from .views.user import UserRegisterView
urlpatterns = [
    path('user/register/', UserRegisterView.as_view()),
]