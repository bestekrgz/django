from django.apps import AppConfig


class YourturnappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'yourturnapp'

    def ready(self):
        import users.signals
