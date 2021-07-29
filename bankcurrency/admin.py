from django.contrib import admin
from .models import Company, AlfaBank, AlfaBankUnAuth, Date


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AlfaBankAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'company', 'eur_buy', 'eur_sell', 'usd_buy', 'usd_sell', 'rur_buy', 'rur_sell')
    list_display_links = ('id', 'date')
    search_fields = ('date', 'id')  # по каким полям мы можем искать


class DateAdmin(admin.ModelAdmin):
    list_display = ('date',)


class AlfaBankUnAuthAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'usd', 'rur', 'eur')


admin.site.register(Company, CompanyAdmin)
admin.site.register(AlfaBank, AlfaBankAdmin)
admin.site.register(Date, DateAdmin)
admin.site.register(AlfaBankUnAuth, AlfaBankUnAuthAdmin)
