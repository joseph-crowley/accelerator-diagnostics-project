from django.core.management.base import BaseCommand
from core.models import CustomUser as User

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username='ucsb_admin').exists():
            User.objects.create_superuser('ucsb_admin', 'crowley@ucsb.edu', 'ucsb2023')
            self.stdout.write(self.style.SUCCESS('Successfully created superuser'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
