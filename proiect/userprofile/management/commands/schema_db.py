import django.apps
from django.contrib.auth.models import User
from django.core.management import BaseCommand


def schema_db():
    all_models = django.apps.apps.get_models()
    print(all_models)
    for model in all_models:
        fields_name = [field.name for field in model._meta.get_fields()]
        list_of_parents = [parent.__name__ for parent in model._meta.get_parent_list()]
        print(fields_name, '=>', model.__name__, list_of_parents)

    return True


class Command(BaseCommand):
    help = 'Dezactivare utilizatori'

    def handle(self, *args, **kwargs):
        schema_db()

# 0 12 * * * root /usr/local/bin/nxportal-command.sh schema_db