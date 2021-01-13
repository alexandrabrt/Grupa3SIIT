from django.db import models

# Create your models here.


class Location(models.Model):

    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    active = models.CharField(default=1, max_length=2)

    def __str__(self):
        return f"{self.city} - {self.country}"
