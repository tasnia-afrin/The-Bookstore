import uuid
from django.db import models
from mainapp.models import CustomUser, BaseModel
from books.models import Book



# Create your models here.
class Reader(models.Model):
    id = models.IntegerField(auto_created='False', primary_key='True')
    uid = models.UUIDField(
        default=uuid.uuid4, editable=True, unique=True, db_index=True
    )
    reader = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='readers', null='True', blank='True')
    intro = models.TextField(null=True, blank=True)


# class Bookmarks(BaseModel):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='current_readers', null='True', blank='True')
#     reader = models.OneToOneField(Reader, on_delete=models.CASCADE, related_name='bookmarked', null='True', blank='True')