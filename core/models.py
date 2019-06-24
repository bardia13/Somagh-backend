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


class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    manager = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='department_manager')
    members = models.ManyToManyField(User, related_name='department')


class Case(models.Model):
    Complaint = 'C'
    Request = 'R'
    Critique = 'Q'
    Suggestion = 'S'
    typeChoices = (
        (Complaint, 'شکایت'),
        (Request, 'درخواست'),
        (Critique, 'انتقاد'),
        (Suggestion, 'پیشنهاد')
    )
    Open = 'O'
    Closed = 'C'
    InQueue = 'I'
    Postponed = 'P'
    statusChoices = (
        (Open, 'باز'),
        (Closed, 'بسته'),
        (InQueue, 'در انتظار'),
        (Postponed, 'به تعویق افتاده')
    )
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='cases')
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, related_name='cases')
    title = models.CharField(max_length=200, null=False)
    type = models.CharField(max_length=1, choices=typeChoices, default=Request)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=False)
    status = models.CharField(max_length=1, choices=statusChoices, default=Open)


# class Refer(models.Model)