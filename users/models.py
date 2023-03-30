from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(verbose_name='First Name', max_length=100)
    last_name = models.CharField(verbose_name='Last Name', max_length=100)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    is_manager = models.BooleanField(default=False)
    is_landlord = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name',]

    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name)
