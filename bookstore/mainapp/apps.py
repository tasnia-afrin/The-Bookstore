from django.apps import AppConfig


class MainappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapp'


    def ready(self):
        """
        Override this method in subclasses to run code when Django starts.
        """
        import mainapp.signals