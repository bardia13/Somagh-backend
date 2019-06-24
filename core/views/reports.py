from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from ..models import Case, Refer
from ..serializers import CaseCreateSerializer, ReferListSerialzier, ActionSerializer, CaseDetailSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from ..filters import CaseFilter
from django_filters import rest_framework as filters
from django.db.models import Q, F, ExpressionWrapper, Count, IntegerField, FloatField

#
# class GetCaseCountComplaints(GenericAPIView):
#     permission_classes = [IsAuthenticated, IsAdminUser]
#
#     def get(self, request):
#         count = Case.objects.filter(type=Case.Complaint)
#         .values('id')
#         .annotate('count' = ExpressionWrapper(Count('id'), output_field=IntegerField()))