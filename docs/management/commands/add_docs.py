from datetime import datetime, timezone, timedelta
from django.core.management.base import BaseCommand
from docs.models import Documentation
import random

class Command(BaseCommand):
    help = 'Populate database with sample docs objects'

    def handle(self, *args, **kwargs):
        base_date = datetime(2023, 10, 1, tzinfo=timezone.utc)

        for i in range(1, 11):
            date_with_offset = base_date + timedelta(days=i-1)
            timestamp_str = date_with_offset.strftime('%Y-%m-%d %H:%M:%S%z')

            type_choice = random.choice(['guide', 'faq', 'tech'])

            Documentation.objects.create(
                title=f'Sample Doc {i} - {type_choice}',
                content=f'Sample content for doc {i}',
                type=type_choice,
                date_created=timestamp_str
            )
        self.stdout.write(self.style.SUCCESS(f'Successfully created sample docs'))
