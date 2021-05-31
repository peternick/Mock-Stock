from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    balance = models.DecimalField(decimal_places=2, max_digits=9)
