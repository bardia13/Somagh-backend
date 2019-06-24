from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Profile, Case, Refer, Department
from django.contrib.auth.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileDetailSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = Profile
        fields = '__all__'


class RegisterUserSerialzier(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=100, write_only=True)
    email = serializers.CharField(max_length=100,write_only=True)
    serial = serializers.CharField(max_length=10, write_only=True)
    first_name = serializers.CharField(max_length=100, write_only=True)
    last_name = serializers.CharField(max_length=100, write_only=True)
    userRole = serializers.CharField(max_length=1, default='S', write_only=True)


    def create(self, validated_data):
        if User.objects.filter(username=validated_data['username']).exists() or \
           User.objects.filter(email=validated_data['email']).exists() or \
           Profile.objects.filter(serial=validated_data['serial']).exists():
            raise ValidationError({"message": "Duplicate"})

        new_user = User.objects.create(username=validated_data['username'],
                                       email=validated_data['email'],
                                       first_name=validated_data['first_name'],
                                       last_name=validated_data['last_name'])
        new_user.set_password(validated_data['password'])
        print(validated_data)
        new_profile = Profile.objects.create(
            user=new_user,
            userRole=validated_data['userRole'],
            serial=validated_data['serial'],
        )

        if (validated_data['userRole'] == Profile.Student):
            new_profile.verified = True
            new_profile.save()

        return {
            'username' : new_user.username,
        }


class CaseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ('creator', 'department', 'title', 'type', 'description',)


class CaseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'


class ReferListSerialzier(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(read_only=True, slug_field='username')
    receiver = serializers.SlugRelatedField(read_only=True, slug_field='username')
    case = CaseDetailSerializer()

    class Meta:
        model = Refer
        fields = ('case', 'date', 'description', 'isLeaf', 'sender', 'reciever')


class ActionSerializer(serializers.Serializer):
    id = serializers.IntegerField(write_only=True)
    case = serializers.PrimaryKeyRelatedField(queryset=Case.objects.all().exclude(status=Case.Closed))
    sender = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=True)
    description = serializers.CharField(max_length=1000, allow_blank=True)
    status = serializers.CharField(max_length=1, allow_blank=True, default="")

    def create(self, validated_data):
        case = validated_data['case']
        currentRefer = None
        try:
            currentRefer = Refer.objects.get(case=case, isLeaf=True)
        except Refer.DoesNotExist:
            pass
        if currentRefer is not None:
            currentRefer.isLeaf = False
        if validated_data['status'] != "" :
            case.status = validated_data['status']
            case.save()

        if validated_data['receiver'] is not None :
            refer = Refer.objects.create(
                case=case,
                sender=validated_data['sender'],
                receiver=validated_data['receiver'],
                description=validated_data['description'],
                isLeaf=True
            )

            return refer

        return {
            "status": case.status
        }



