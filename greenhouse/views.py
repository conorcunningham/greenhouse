from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from . serializers import *
from . models import Sensor, Topic, SensorTopic, SensorValue, TempHum


class SensorViewSet(viewsets.ModelViewSet):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()


class SensorValueViewSet(viewsets.ModelViewSet):
    serializer_class = SensorValueSerializer
    queryset = SensorValue.objects.all()


class SensorTopicViewSet(viewsets.ModelViewSet):
    serializer_class = SensorTopicSerializer
    queryset = SensorTopic.objects.all()


class TempHumViewSet(viewsets.ModelViewSet):
    serializer_class = TempHumSerializer
    queryset = TempHum.objects.all()


@permission_classes([AllowAny])
def aruba_alerts():
    return Response({"Greeting": "Hello from my greenhouse!"})