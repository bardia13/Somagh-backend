from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from ..models import Profile, Department
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from ..serializers import RegisterUserSerialzier, ProfileDetailSerializer,DepartmentDetailSerializer, UserMinimalSerializer


class CurrentProfileDetail(RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ProfileDetailSerializer

    def get_object(self):
        return Profile.objects.get(user=self.request.user)


class UserRegisterView(CreateAPIView):
    permission_classes = []
    serializer_class = RegisterUserSerialzier


class ProfileList(ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ProfileDetailSerializer
    queryset = Profile.objects.all()


class StaffProfileMinimalList(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserMinimalSerializer
    queryset = User.objects.filter(is_staff=True)


class RetrieveProfile(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ProfileDetailSerializer

    def get_object(self, pk):
        try:
            return Profile.objects.get(user_id=pk)
        except Profile.DoesNotExist:
            raise Http404


class DeleteProfile(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ProfileDetailSerializer

    def get_object(self, pk):
        try:
            return Profile.objects.get(user_id=pk)
        except Profile.DoesNotExist:
            raise Http404


class DeactiveProfile(GenericAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, pk):
        profile = Profile.objects.get(user_id=pk)
        profile.user.is_active = False
        return Response({"message" : "done"}, status=status.HTTP_200_OK)


class ConfitmProfile(GenericAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, pk):
        profile = Profile.objects.get(user_id=pk)
        profile.user.is_active = True
        return Response({"message" : "done"}, status=status.HTTP_200_OK)


class ListDepartments(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = DepartmentDetailSerializer
    queryset = Department.objects.all()
