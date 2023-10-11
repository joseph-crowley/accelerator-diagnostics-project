from datetime import datetime, timezone, timedelta
from django.core.management.base import BaseCommand
from analysis.models import DataRecord
import random

class Command(BaseCommand):
    help = 'Populate database with sample DataRecord objects'

    def handle(self, *args, **kwargs):
        base_date = datetime(2022, 1, 1, tzinfo=timezone.utc)

        for i in range(1, 11):
            date_with_offset = base_date + timedelta(days=i-1)
            timestamp_str = date_with_offset.strftime('%Y-%m-%d %H:%M:%S%z')

            DataRecord.objects.create(
                run_id=i,
                timestamp=timestamp_str,
                data_values=[
                    {"temperature": random.randint(20, 30), "humidity": random.randint(40, 60)},
                    {"temperature": random.randint(20, 30), "humidity": random.randint(40, 60)}
                ],
                anomalies={}
            )
        self.stdout.write(self.style.SUCCESS(f'Successfully created sample DataRecords'))
