from django.urls import path, include
from .views.user import UserRegisterView
from .views.case import CaseCreate, ReferList, Action
urlpatterns = [
    path('user/register/', UserRegisterView.as_view()),
    path('case/create/', CaseCreate.as_view()),
    path('case/action/', Action.as_view()),
    path('refer/list/', ReferList.as_view()),
]