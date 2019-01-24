from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):
    user_name = models.ForeignKey(User,unique = True, related_name = 'user_name' , on_delete=models.CASCADE)
    follows = models.ManyToManyField(User, related_name = 'follows', symmetrical=False )
