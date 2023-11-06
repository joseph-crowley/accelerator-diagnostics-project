from django.core.management.base import BaseCommand
from analysis.models import Run
from experiment.models import DiRPiConfiguration

class Command(BaseCommand):
    help = 'Populate database with sample Run objects'

    def handle(self, *args, **kwargs):
        # Get the default DiRPiConfiguration instance if it exists, or create a new one.
        config, created = DiRPiConfiguration.objects.get_or_create(
            name="Default Config",  # This is just an example identifier. 
            defaults={
                'description': 'This is the default configuration.',
                'events_per_file': 1,
                'memory_depth': 1,
                'software_trigger': False,
                'external_trigger': False,
                'trigger_channel1': False,
                'trigger_channel2': False,
                'prescale': 1,
                'trigger_position': 1,
                'dac_value_channel1': 0,
                'dac_value_channel2': 0,
                'pedestal_channel1': 0,
                'pedestal_channel2': 0,
                'sipm_bias_channel1': 0,
                'sipm_bias_channel2': 0,
                'dac_pulse_channel1': 0,
                'dac_pulse_channel2': 0,
                'clock_speed': 0,
            }
        )

        for i in range(1, 11):
            Run.objects.create(
                notes=f"Sample Notes {i}",
                configuration=config,
                status='queued'
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully created sample Runs'))
