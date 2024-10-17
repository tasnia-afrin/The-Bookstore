import uuid

from django.contrib.auth.models import AbstractUser 
from django.db import models
from django.utils import timezone 
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
from .choices import *

# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, db_index=True
    )
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        abstract=True


class CustomUser(AbstractUser, BaseModel):
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']    

    email = models.EmailField(_('email address'), unique=True, blank=True)
    username = models.CharField(max_length=100, unique='False', blank='True')
    first_name = models.CharField(max_length=150, null=False, blank='True')
    last_name = models.CharField(max_length=150, null=False, blank='True')       

    user_type = models.CharField( 
        max_length = 20, 
        choices = USER_TYPE_CHOICES,         
        ) 

    objects = CustomUserManager()
