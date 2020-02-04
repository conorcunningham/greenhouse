from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=32, unique=True)
    type = models.CharField(max_length=32)


class Sensor(models.Model):
    name = models.CharField(max_length=32, unique=True)
    type = models.CharField(max_length=32)

    def __str__(self) -> str:
        return f"{self.name} of type {self.type}"


class Topic(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)

    def __str__(self) -> str:
        return f"{self.name}"


class Actuator(models.Model):
    pass


class Pump(models.Model):
    pass


class SensorValue(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)


class SensorTopic(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Sensor Topic'
        verbose_name_plural = 'Sensor Topics'

    def __str__(self):
        return f"{self.sensor} subscribed to {self.topic}"


class TempHum(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Temperature Humidity Reading'
        verbose_name_plural = 'Temperature Humidity Readings'

    def __str__(self):
        return f"{self.sensor.name} {self.temp} degrees {self.humidity}% humidity"


