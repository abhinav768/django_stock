from django.core.exceptions import ValidationError
from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    # name = models.CharField(max_length=100)

    # def save(self, *args, **kwargs):
    #     if Stock.objects.filter(ticker=self.ticker).exists():
    #         raise ValidationError('Stock with this symbol already exists.')
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.ticker
