from rest_framework.routers import SimpleRouter
from django.urls import path, include
from . views import *

router = SimpleRouter(trailing_slash=False)
router.register("sensors", SensorViewSet, basename="sensors")
router.register("topics", TopicViewSet, basename="topics")
router.register("sensor-topics", SensorTopicViewSet, basename="sensors_topics")
router.register("sensor-values", SensorValueViewSet, basename="sensors_value")
router.register("temperatures", TempHumViewSet, basename="temperatures")

urlpatterns = [
    path("", include(router.urls)),
]
