from django.core.management.base import BaseCommand
from core.models import TeamMember

class Command(BaseCommand):
    help = 'Create initial team members'

    def handle(self, *args, **kwargs):
        # Add Joe Crowley
        joe = TeamMember.objects.create(
            name='Joe Crowley',
            contact_info='crowley@ucsb.edu',
            description="Joe has a passion for nature, science, music, and travel. He is currently pursuing a PhD in Physics at UCSB. His research interests include High Energy Physics Experiment, High Performance Computing, Machine Learning, and Dynamical Systems.",
        )
        image_path = 'staticfiles/images/joe_crowley.jpg'
        with open(image_path, 'rb') as f:
            joe.image.save('joe_crowley.jpg', f, save=True)
        joe.save()

        # Add David Stuart
        david = TeamMember.objects.create(
            name='David Stuart',
            contact_info='davidstuart@ucsb.edu',
            description="David is a Professor of Physics at UCSB in the High Energy Physics Experiment Group. In his career he investigates the nature of the universe at the most fundamental scales, exploring particle collisions at the CERN Large Hadron Collider.",
        )
        image_path = 'staticfiles/images/david_stuart.jpg'
        with open(image_path, 'rb') as f:
            david.image.save('david_stuart.jpg', f, save=True)
        david.save()


        self.stdout.write(self.style.SUCCESS('Successfully created team members'))
