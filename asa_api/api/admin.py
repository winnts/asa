from django.contrib import admin
from .models import Currency

# Register your models here.


class CurrencyAdmin(admin.ModelAdmin):
    list = ('name', 'dqte', 'sell', 'buy')

    admin.site.register(Currency)
