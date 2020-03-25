from django.db import models
from django.utils import timezone
from users.models import CustomUser
from django.urls import reverse


class Room(models.Model):
    description = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name