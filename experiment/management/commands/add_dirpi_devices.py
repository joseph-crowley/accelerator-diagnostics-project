from django.core.management.base import BaseCommand
from django.utils import timezone
import random
from experiment.models import DiRPiDevice, DiRPiGroup, DiRPiConfiguration

class Command(BaseCommand):
    help = 'Adds 3 dummy DiRPi devices to the database'

    def handle(self, *args, **kwargs):
        configuration = DiRPiConfiguration.objects.first()
        if not configuration:
            self.stdout.write(self.style.ERROR('Configuration not found. Please add it first.'))
            return

        groups = DiRPiGroup.objects.all()
        if not groups.exists():
            self.stdout.write(self.style.ERROR('Groups not found. Please run add_dirpi_groups command first.'))
            return

        for i in range(1, 4):
            group = groups[i % groups.count()]  # Assigning groups in a round-robin fashion

            # Build device object and add to group before saving  
            device = DiRPiDevice(  
                device_number=i,  
                group=group,
                device_ip=f'192.168.1.{i}',  
                configuration=configuration,  
                status='active',  
                last_ping_time=timezone.now(),  
                health_status='good',  
                current_run_number=random.randint(1, 100)  
            )  
            device.save()  
            group.devices.add(device)  
            group.save()  

            self.stdout.write(self.style.SUCCESS(f'Device {device.device_id} added to group {group.group_name} successfully.'))
