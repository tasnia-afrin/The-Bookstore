from django.db import models

from authors.models import Author
from mainapp.models import BaseModel
from mainapp.choices import VIEW_PERMISSION_CHOICES

# Create your models here.
class Book(BaseModel):
    name = models.TextField(verbose_name='Name of the Book')
    writer = models.ManyToManyField(Author, related_name='books', null='True', blank='True')
    genre = models.TextField(null=True, blank=True)
    intro = models.TextField(null=True, blank=True)
    view_permission = models.CharField(
        max_length=20,
        choices=VIEW_PERMISSION_CHOICES,
    )


class Chapters(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters', null='True', blank='True')
    title = models.TextField(verbose_name='Chapter No. and Title', null=True, blank=True)
