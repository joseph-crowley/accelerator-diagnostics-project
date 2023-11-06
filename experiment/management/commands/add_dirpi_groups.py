
from django.core.management.base import BaseCommand  
from core.models import CustomUser as User
from experiment.models import DiRPiGroup, DiRPiDevice  

class Command(BaseCommand):  
    help = 'Adds groups from a sample'  

    def handle(self, *args, **options):  
        groups = [
            {
              "group_name": "LANL",
              "location": "Los Alamos",
              "health_status": "healthy",
              "password": "pass123LANL",
            },
            {
              "group_name": "FEL",
              "location": "Free Electron Laser",
              "health_status": "healthy",
              "password": "pass123FEL",
            },
            {
              "group_name": "CNL",
              "location": "Crocker Nuclear Lab",
              "health_status": "healthy",
              "password": "pass123CNL",
            }
        ]

        for g in groups:  
            group_name = g["group_name"]  
            location = g["location"]  
            health_status = g["health_status"]  
            password = g["password"]

            group = DiRPiGroup(  
                group_name=group_name,  
                location=location,  
                health_status=health_status,
                password=password
            )  
            group.save()  

            # Set Many-to-Many Relationships for users
            # Here, you should ensure that the user IDs provided actually exist.
            associated_user_ids = g.get("associated_users", [])
            if associated_user_ids:
                associated_users = User.objects.filter(id__in=associated_user_ids)
                group.associated_users.set(associated_users)
            else: 
                group.associated_users.set(User.objects.all())

            self.stdout.write(self.style.SUCCESS(f'Successfully added group {group_name}'))
