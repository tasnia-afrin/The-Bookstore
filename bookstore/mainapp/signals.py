from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser
from authors.models import Author
from readers.models import Reader


@receiver(post_save, sender=CustomUser)
def create_user_profile(instance, sender, created, **kwargs):
    if created:
        if not instance.is_superuser: 
            if instance.user_type == "author":
                Author.objects.get_or_create(
                    author=instance, id=instance.id, uid=instance.uid
                )
            elif instance.user_type == "reader":
                Reader.objects.get_or_create(
                    reader=instance, id=instance.id, uid=instance.uid
                )
