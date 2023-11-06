
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from experiment.models import DiRPiGroup

class DiRPiGroupListView(LoginRequiredMixin, View):
    """
    View to list all DiRPi Groups accessible to the authenticated user.
    """
    template_name = 'dirpi_group_list.html'
    
    def get(self, request, *args, **kwargs):
        """
        Handle GET requests.
        """
        # Fetch all DiRPiGroup objects for the authenticated user
        groups = DiRPiGroup.objects.filter(associated_users=request.user)
        return render(request, self.template_name, {'groups': groups})
