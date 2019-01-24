from django.contrib import admin
from .models import Post,UserType
# Register your models here.
class UserTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserType._meta.get_fields()]

class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.get_fields()]

admin.site.register(UserType, UserTypeAdmin)
admin.site.register(Post,PostAdmin)
