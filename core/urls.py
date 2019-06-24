from django.urls import path, include
from .views.user import UserRegisterView, CurrentProfileDetail
from .views.case import CaseCreate, ReferList, Action, CaseList, CaseChangeSatisfied

urlpatterns = [
    path('user/register/', UserRegisterView.as_view()),
    path('user/detail/', CurrentProfileDetail.as_view()),
    path('case/create/', CaseCreate.as_view()),
    path('case/list/', CaseList.as_view()),
    path('case/list/satisfied/', CaseChangeSatisfied.as_view()),
    path('case/action/', Action.as_view()),
    path('refer/list/', ReferList.as_view()),
]
