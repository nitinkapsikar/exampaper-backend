from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from django.contrib.auth.models import User
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username='kapsikar',
                password='nitin1234',
                email='kapsikarpk@gmail.com'
            )
