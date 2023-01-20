from django.apps import AppConfig


class AnvandareConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'anvandare'

    def ready(self):
        import anvandare.signals
