from django.shortcuts import render
from rest_framework import generics, viewsets
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

