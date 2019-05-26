from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from datetime import datetime, time


class Profile(models.Model):
    Worker = 'W'
    Teacher = 'T'
    Student = 'S'
    Manager = 'M'
    userRoleChoices = (
        (Worker, 'کارمند'),
        (Teacher, 'استاد'),
        (Student, 'دانشجو'),
        (Manager, 'مدیر'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    serial = models.CharField(max_length=10, null=False)
    nationalId = models.CharField(max_length=10, null=True, blank=True)
    userRole = models.CharField(max_length=1, choices=userRoleChoices, default=Manager)
    verified = models.BooleanField(default=False)
