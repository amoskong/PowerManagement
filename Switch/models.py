from django.db import models

# Create your models here.

class Switch(models.Model):
    state = models.IntegerField(default=0)
