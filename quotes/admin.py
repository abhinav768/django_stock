from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Stock

class StockAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if change:  # If the object is being changed (edited)
            existing_stock = Stock.objects.filter(ticker=obj.ticker).exclude(pk=obj.pk).first()
            if existing_stock:
                form.errors['ticker'] = form.error_class(['Stock with this symbol already exists.'])
                return
        else:  # If the object is being added (created)
            if Stock.objects.filter(ticker=obj.ticker).exists():
                form.errors['ticker'] = form.error_class(['Stock with this symbol already exists.'])
                return

        # Call the superclass method to handle saving
        super().save_model(request, obj, form, change)

admin.site.register(Stock, StockAdmin)
