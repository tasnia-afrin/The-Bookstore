from .models import Blog
from authors.models import Author

class BlogServices:

    def create_blog(
        self,
        author: Author,
        blog: str,
        view_permission: str,
    ) -> Blog:
        return Blog.objects.create(
            author=author, blog=blog, view_permission=view_permission
        )
