from django.db import models
import decimal

class Stock(models.Model):
    stock_ticker = models.CharField(max_length=6)
    company_name = models.CharField(max_length=40)
    number_stocks = models.PositiveIntegerField()
    total_value = models.DecimalField(decimal_places=2, max_digits=12)

    def __str__(self) -> str:
        return self.stock_ticker
    
    def get_num_stocks(self):
        return int(self.number_stocks)

    def get_total_val(self):
        return float(self.total_value)    
    
    def set_num_stocks(self, num_stocks):
        self.number_stocks = num_stocks

    def set_total_val(self, value):
        self.total_value = decimal.Decimal(value)  
        

class Account(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    balance = models.DecimalField(decimal_places=2, max_digits=12)
    account_value = models.DecimalField(decimal_places=2, max_digits=12, default=10000)
    owned_stocks = models.ManyToManyField(Stock, db_table='stock_table', blank=True)

    def __str__(self) -> str:
        return self.username
    
    def get_account_val(self):
        return float(self.account_value)
    
    def get_balance(self):
        return float(self.balance)
