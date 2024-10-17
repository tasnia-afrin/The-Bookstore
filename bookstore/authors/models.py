import uuid
from django.db import models
from mainapp.models import BaseModel, CustomUser

class Author(models.Model):
    id = models.IntegerField(auto_created='False', primary_key='True')
    uid = models.UUIDField(
        default=uuid.uuid4, editable=True, unique=True, db_index=True
    )
    author = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='authors', null='True', blank='True')    
    biography = models.TextField(verbose_name='Short Biography', null='True', blank='True')
    dob = models.TextField(verbose_name='Date of Birth', null='True', blank='True')
    


  