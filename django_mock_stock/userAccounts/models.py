from django.db import models


class Stock(models.Model):
    stock_ticker = models.CharField(max_length=6)
    company_name = models.CharField(max_length=40)
    number_stocks = models.PositiveIntegerField()
    total_value = models.DecimalField(decimal_places=2, max_digits=12)

    def __str__(self) -> str:
        return self.stock_ticker


class Account(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    balance = models.DecimalField(decimal_places=2, max_digits=12) #why does this not need a default?
    account_value = models.DecimalField(decimal_places=2, max_digits=12, default=10000.00)
    owned_stocks = models.ManyToManyField(Stock, db_table='stock_table', blank=True)

    def __str__(self) -> str:
        return self.username
    
