from django.db.models import QuerySet
from authors.models import Author
from .models import Book

class BookServices:

    def create_book(
            self,
            name: str,
            writer: Author,
            genre: str = "",
            intro: str = "",
    ): Book.objects.create( 
        name=name, writer=writer, genre=genre, intro=intro
    )

    