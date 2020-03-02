from django.shortcuts import render
from rest_framework import generics, viewsets
from . serializers import *
from . models import Sensor, Topic, SensorTopic, SensorValue, TempHum
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from statistics import mean


class HomePageView(TemplateView):
    template_name = "home.html"
    login_url = "accounts/login/"


class PropagatorView(TemplateView):
    template_name = "propagator.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        temp = []
        hum = []
        time = []
        for pair in TempHum.objects.all():
            temp.append(float(pair.temperature.normalize()))
            hum.append(float(pair.humidity.normalize()))
            time.append(str(pair.timestamp.strftime("%H:%M:%S")))
        print(time)
        print(len(time))
        context['name'] = "Propagator"
        context['temp'] = temp
        context['hum'] = hum
        context['time'] = time
        context['avg_temp'] = round(mean(temp), 2)
        context['avg_hum'] = round(mean(hum), 2)
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

