from django.shortcuts import render
from rest_framework import generics, viewsets
from . serializers import *
from . models import Sensor, Topic, SensorTopic, SensorValue, TempHum
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class PropagatorView(TemplateView):
    template_name = "propagator.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        temp = []
        hum = []
        time = []
        for pair in TempHum.objects.all():
            temp.append(int(pair.temperature.normalize()))
            hum.append(int(pair.humidity.real.normalize()))
            time.append(str(pair.timestamp.strftime("%H:%M:%S")))
        print(time)
        print(len(time))
        context['temp'] = temp
        context['hum'] = hum
        context['time'] = time
        context['data'] = TempHum.objects.all()

        return context


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

