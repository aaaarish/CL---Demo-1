from rest_framework.serializers import ModelSerializer
from .models import Device, DeviceHealth


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class DeviceHealthSerializer(ModelSerializer):
    class Meta:
        model = DeviceHealth
        fields = "__all__"


class DeviceHealthSerializer(ModelSerializer):
    class Meta:
        model = DeviceHealth
        fields = "__all__"