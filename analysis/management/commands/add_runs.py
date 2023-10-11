from django.core.management.base import BaseCommand
from analysis.models import Run

class Command(BaseCommand):
    help = 'Populate database with sample Run objects'

    def handle(self, *args, **kwargs):
        for i in range(1,11):
            Run.objects.create(
                metadata=f"Sample Metadata {i}",
                configurations=f"Sample Config {i}",
                #associated_group_id=1,
                tags=['sample'],
                status='active'
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully created sample Runs'))
