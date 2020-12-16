from django.db import models

# Create your models here.
from aplicatie1.models import Location

companies_choices = (('S.R.L.', 'S.R.L.'), ('S.A.', 'S.A.'))


class Companies(models.Model):

    name = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=companies_choices)
    active = models.BooleanField(default=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} from {self.location.city} city  - {self.location.country} country"
