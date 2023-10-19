from django.db import models
from django.contrib.auth.models import User
import uuid
from users.models import Profile


# Create your models here.
class LoginInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fails = models.PositiveSmallIntegerField(default=0)
    login_link = models.CharField(unique=True, blank=True, null=True, max_length=225)
    reset_link = models.CharField(unique=True, blank=True, null=True, max_length=225)

    def __str__(self):
        return self.user.username
