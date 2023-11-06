from django.http import HttpResponseForbidden

from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from experiment.models import DiRPiGroup

class DiRPiGroupMonitorView(LoginRequiredMixin, View):
    """
    View to monitor all DiRPi Devices in a specific DiRPi Group.
    """
    template_name = 'dirpi_group_monitor.html'
    
    def get(self, request, group_id, *args, **kwargs):
        """
        Handle GET requests.
        """
        # Fetch the specific DiRPiGroup object by its ID
        group = get_object_or_404(DiRPiGroup, id=group_id)
        
        if not request.user.has_perm('can_view_group'):
            return HttpResponseForbidden("You don't have permission to view this page.")
                # Check if the authenticated user is associated with this group
        if request.user not in group.associated_users.all():
            return HttpResponseForbidden("You don't have permission to view this page.")
        
        return render(request, self.template_name, {'group': group})
