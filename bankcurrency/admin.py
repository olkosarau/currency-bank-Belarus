from django.contrib import admin
from .models import CurrencyAuthUser, CurrencyUnAuthUser


class CurrencyAuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'date', 'eur_buy', 'eur_sell', 'usd_buy', 'usd_sell', 'rur_buy', 'rur_sell')
    list_display_links = ('id', 'date')
    search_fields = ('id', 'date')


class CurrencyUnAuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'date', 'usd', 'rur', 'eur')


admin.site.register(CurrencyAuthUser, CurrencyAuthUserAdmin)
admin.site.register(CurrencyUnAuthUser, CurrencyUnAuthUserAdmin)
