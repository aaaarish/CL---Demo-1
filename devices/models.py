from django.db import models


# Create your models here.
class Device(models.Model):
    device_name = models.CharField(max_length=255)
    device_id = models.CharField(max_length=255)
    issuance_date = models.CharField(max_length=255)
    status = models.CharField(max_length=255)


class DeviceHealth(models.Model):
    name = models.ForeignKey(Device, on_delete=models.CASCADE, default=None)
    temperature = models.CharField(max_length=255)
    active_duration = models.CharField(max_length=255)
    total_active_duration = models.CharField(max_length=255)
    last_maintenance_date = models.CharField(max_length=255)
    storage_capacity = models.CharField(max_length=255)
    total_recordings = models.CharField(max_length=255)
    last_transfer_status = models.CharField(max_length=255)


