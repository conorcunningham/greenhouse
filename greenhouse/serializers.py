from . models import *
from rest_framework import serializers


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ("id", "name", "type")


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ("id", "name", "description")


class SensorValueSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer()

    class Meta:
        model = SensorValue
        fields = ("id", "sensor", "value", "unit", "timestamp")


class SensorTopicSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer()

    class Meta:
        model = SensorTopic
        fields = ("id", "sensor", "topic")


class TempHumSerializer(serializers.ModelSerializer):

    class Meta:
        model = TempHum
        fields = ("id", "sensor", "temperature", "humidity", "timestamp")
