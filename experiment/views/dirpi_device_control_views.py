
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

from experiment.models import DiRPiDevice
from experiment.forms import DiRPiDeviceForm

class DiRPiDeviceControlView(LoginRequiredMixin, View):
    """
    View to control a specific DiRPi Device.
    """
    template_name = 'dirpi_device_control.html'
    
    def get(self, request, device_id, *args, **kwargs):
        """
        Handle GET requests.
        """
        # Fetch the specific DiRPiDevice object by its ID
        device = get_object_or_404(DiRPiDevice, pk=device_id)
        
        # Check if the authenticated user is associated with the group that owns this device
        if request.user not in device.group.associated_users.all():
            return HttpResponseForbidden("You don't have permission to view this page.")
        
        form = DiRPiDeviceForm(instance=device)
        return render(request, self.template_name, {'device': device, 'form': form})
        
    def post(self, request, device_id, *args, **kwargs):
        """
        Handle POST requests.
        """
        device = get_object_or_404(DiRPiDevice, pk=device_id)
        form = DiRPiDeviceForm(request.POST, instance=device)
        
        if form.is_valid():
            # Only send the configuration if it has changed  
            if form.has_changed():  
                form.save()  
                device.send_configuration()  
            return redirect('dirpi_group_monitor', device.group.id)  
        
        return render(request, self.template_name, {'device': device, 'form': form})
