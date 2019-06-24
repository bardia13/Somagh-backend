from django.contrib import admin

from .models import Case, Profile, Refer, Department
# Register your models here.

admin.site.register(Case)
admin.site.register(Profile)
admin.site.register(Refer)
admin.site.register(Department)