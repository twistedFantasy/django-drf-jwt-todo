import os

from django.core.management.base import BaseCommand

from todo.users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if os.environ.get('SYSTEM_EMAIL') and os.environ.get('SYSTEM_PASSWORD'):
            if not User.objects.filter(email=os.environ['SYSTEM_EMAIL']).exists():
                User.objects.create_superuser(os.environ['SYSTEM_EMAIL'], os.environ['SYSTEM_PASSWORD'])
