from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.

class UserAccount(AbstractUser):
    first_name = models.CharField(verbose_name="First Name", max_length=100)
    last_name = models.CharField(verbose_name="Last Name", max_length=100)
    email = models.EmailField(verbose_name="User Email", max_length=254, unique=True)
    is_manager = models.BooleanField(default=False)
    is_landlord = models.BooleanField(default=False)
    username = None
    
    objects = UserManager()
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]
    
    # update django about user model
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
    
    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name)