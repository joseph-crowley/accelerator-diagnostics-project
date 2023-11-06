
from django.test import TestCase
from experiment.models import DiRPiDevice
import uuid

class DiRPiDeviceTestCase(TestCase):
    def setUp(self):
        self.device_id = uuid.uuid4()
        DiRPiDevice.objects.create(device_id=self.device_id)

    def test_device_creation(self):
        """Test the creation of a DiRPiDevice object."""
        device = DiRPiDevice.objects.get(device_id=self.device_id)
        self.assertEqual(device.device_id, self.device_id)
