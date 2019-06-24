from django.urls import path, include
from .views.user import UserRegisterView
from .views.case import CaseCreate, ReferList
urlpatterns = [
    path('user/register/', UserRegisterView.as_view()),
    path('case/create/', CaseCreate.as_view()),
    path('refer/list/', ReferList.as_view()),
]