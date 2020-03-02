from django.contrib import admin
from . models import *


class SensorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type")


class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")


class SensorValueAdmin(admin.ModelAdmin):
    list_display = ("id", "sensor", "value", "unit", "timestamp")


class SensorTopicAdmin(admin.ModelAdmin):
    list_display = ("id", "sensor", "topic")


class TempHumAdmin(admin.ModelAdmin):
    list_display = ("id", "sensor", "temperature", "humidity", "timestamp")


class WebhookAdmin(admin.ModelAdmin):
    list_display = ("id", "params", "data")


admin.site.register(Webhook, WebhookAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(SensorValue, SensorValueAdmin)
admin.site.register(SensorTopic, SensorTopicAdmin)
admin.site.register(TempHum, TempHumAdmin)
