from rest_framework.generics import CreateAPIView
from ..models import Profile
from django.contrib.auth.models import User
from ..serializers import RegisterUserSerialzier


class  UserRegisterView(CreateAPIView):
    permission_classes = []
    serializer_class = RegisterUserSerialzier