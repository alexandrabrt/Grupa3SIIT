from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from aplicatie2.models import Companies


class UserExtend(User):

    customer = models.ForeignKey('aplicatie2.Companies', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.customer.name}'


class Logs(models.Model):

    action_choice = (('created', 'created'), ('updated', 'updated'), ('refresh', 'refresh'))

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey(UserExtend, on_delete=models.CASCADE)
    customer = models.ForeignKey(Companies, on_delete=models.CASCADE)
    action = models.CharField('Action', max_length=10, choices=action_choice)
    url = models.CharField('URL', max_length=100)
