from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from . serializers import *
from . models import Sensor, Topic, SensorTopic, SensorValue, TempHum
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from statistics import mean
from django.utils.html import escape


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


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def aruba_alerts(request):
    Webhook(params=str(request.query_params), data=str(request.data)).save()
    # print(str(request.data))
    # print(str(request.query_params))
    return Response({"Greeting": "Hello from my greenhouse!"})