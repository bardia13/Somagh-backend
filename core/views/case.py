from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from ..models import Case, Refer
from ..serializers import CaseCreateSerializer, ReferListSerialzier
from rest_framework.permissions import IsAuthenticated


class CaseCreate(CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CaseCreateSerializer
    queryset = Case.objects.all()


class ReferList(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ReferListSerialzier

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Refer.objects.all().order_by('-date')
        else:
            return Refer.objects.filter(receiver=user).order_by('-date')

