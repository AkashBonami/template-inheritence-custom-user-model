from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from .manager import customUserManager

class customUser(AbstractUser):
    name=models.CharField(max_length=128,blank = False)
    email=models.CharField(max_length=128, blank=False, unique=True, null=False)
    password=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS= ['name']
    objects=customUserManager()
    def __str__(self):
        return self.email
    
    
