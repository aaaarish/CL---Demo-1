from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DeviceSerializer, DeviceHealthSerializer
from .models import Device, DeviceHealth
from rest_framework import generics


class Status(generics.ListAPIView):

    serializer_class = DeviceSerializer

    def get_queryset(self):
        """
        This view should return a list of all the devices.
        """
        device_status = Device.objects.filter()
        return device_status


class Health(generics.ListAPIView):

    serializer_class = DeviceHealthSerializer

    def get_queryset(self):
        """
        This view should return a list of all the devices.
        """
        device_health = DeviceHealth.objects.filter(name=2)
        return device_health




