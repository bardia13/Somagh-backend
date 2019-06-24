from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from ..models import Case, Refer
from ..serializers import CaseCreateSerializer, ReferListSerialzier, ActionSerializer, CaseDetailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from ..filters import CaseFilter
from django_filters import rest_framework as filters


class CaseCreate(CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CaseCreateSerializer
    queryset = Case.objects.all()


class CaseList(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CaseDetailSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CaseFilter

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Case.objects.all().order_by('-date')
        else:
            return Case.objects.filter(creator=user).order_by('-date')


class CaseChangeSatisfied(GenericAPIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        user = self.request.user
        satisfied = self.request.data.get('satisfied')
        case = self.request.data.get('case')
        case_obj = Case.objects.get(id=case, user=user)
        case_obj.satisfied = satisfied
        return Response(status=status.HTTP_200_OK)


class ReferList(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ReferListSerialzier

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Refer.objects.all().order_by('-date')
        else:
            return Refer.objects.filter(receiver=user).order_by('-date')


class Action(CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ActionSerializer

    def create(self, request, *args, **kwargs):
        receiver = self.request.data.get('receiver', None)
        if receiver is None:
            receiver = self.request.user
        sender = self.request.user
        serializer = self.get_serializer(data=request.data, receiver=receiver, sender=sender)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
