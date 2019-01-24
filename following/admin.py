from django.contrib import admin
from .models import Userprofile
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name']

admin.site.register(Userprofile,UserProfileAdmin)
