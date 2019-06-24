from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from ..models import Profile
from django.contrib.auth.models import User
from ..serializers import RegisterUserSerialzier, ProfileDetailSerializer


class CurrentProfileDetail(RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ProfileDetailSerializer

    def get_object(self):
        return self.request.user.profile


class UserRegisterView(CreateAPIView):
    permission_classes = []
    serializer_class = RegisterUserSerialzier
