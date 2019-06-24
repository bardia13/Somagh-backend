from django_filters import rest_framework as filters
from .models import Case,User,Profile,Refer
from django.db.models import Count
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime


class CaseFilter(filters.FilterSet):
    status = filters.MultipleChoiceFilter(choices=Case.statusChoices)
    creator = filters.NumberFilter()
    department = filters.NumberFilter()

    class Meta:
        model = Case
        fields = ('status', 'creator', 'department')
