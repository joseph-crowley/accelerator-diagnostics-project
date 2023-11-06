
from django.urls import path
from .views import DiRPiGroupListView, DiRPiGroupMonitorView, DiRPiDeviceControlView

urlpatterns = [
    path('', DiRPiGroupListView.as_view(), name='experiment_home'),
    path('group_list/', DiRPiGroupListView.as_view(), name='dirpi_group_list'),
    path('group_monitor/<int:group_id>/', DiRPiGroupMonitorView.as_view(), name='dirpi_group_monitor'),
    path('device_control/<uuid:device_id>/', DiRPiDeviceControlView.as_view(), name='dirpi_device_control'),
]
