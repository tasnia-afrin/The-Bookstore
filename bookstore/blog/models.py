from django.db import models
from mainapp.models import BaseModel
from authors.models import Author
from mainapp.choices import VIEW_PERMISSION_CHOICES

# Create your models here.
class Blog(BaseModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blogs', null='True', blank='True')
    blog = models.TextField(null=True, blank=True)
    view_permission = models.CharField(
        max_length=20,
        choices=VIEW_PERMISSION_CHOICES,
    )
