from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    points = models.IntegerField(default=0)

    def user_id(self):
        return self.id.__str__()