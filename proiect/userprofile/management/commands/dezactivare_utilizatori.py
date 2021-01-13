from django.contrib.auth.models import User
from django.core.management import BaseCommand


def dezactivare_utilizatori():
    User.objects.filter(is_superuser=0).update(is_active=0)
    return True


class Command(BaseCommand):
    help = 'Dezactivare utilizatori'

    def handle(self, *args, **kwargs):
        dezactivare_utilizatori()
