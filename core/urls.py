from django.urls import path, include
from .views.user import UserRegisterView, CurrentProfileDetail, RetrieveProfile, ConfitmProfile, DeactiveProfile,\
    DeleteProfile, ListDepartments
from .views.case import CaseCreate, ReferList, Action, CaseList, CaseChangeSatisfied

urlpatterns = [
    path('user/register/', UserRegisterView.as_view()),
    path('user/detail/', CurrentProfileDetail.as_view()),
    path('user/detail/<int:pk>/', RetrieveProfile.as_view()),
    path('user/confirm/<int:pk>/', ConfitmProfile.as_view()),
    path('user/deactive/<int:pk>/', DeactiveProfile.as_view()),
    path('user/delete/<int:pk>/', DeleteProfile.as_view()),
    path('department/all/', ListDepartments.as_view()),
    path('case/create/', CaseCreate.as_view()),
    path('case/list/', CaseList.as_view()),
    path('case/list/satisfied/', CaseChangeSatisfied.as_view()),
    path('case/action/', Action.as_view()),
    path('refer/list/', ReferList.as_view()),
]
