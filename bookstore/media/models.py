from django.db import models
from mainapp.models import BaseModel
from books.models import Book
from authors.models import Author

class BookFile(BaseModel):
    book = models.OneToOneField(
        Book,
        on_delete=models.CASCADE,
        related_name="pdf",
        null="True",
        blank="True",
    )    
    file =  models.FileField(null=True, blank=True)
