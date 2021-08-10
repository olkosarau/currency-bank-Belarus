from django.contrib import admin
from .models import Company, AlfaBank, AlfaBankUnAuth, BelApb, BelApbUnAuth, BelBank, BelBankUnAuth


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AlfaBankAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'company', 'eur_buy', 'eur_sell', 'usd_buy', 'usd_sell', 'rur_buy', 'rur_sell')
    list_display_links = ('id', 'date')
    search_fields = ('date', 'id')


class AlfaBankUnAuthAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'usd', 'rur', 'eur')


class BelApbAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'company', 'eur_buy', 'eur_sell', 'usd_buy', 'usd_sell', 'rur_buy', 'rur_sell')
    list_display_links = ('id', 'date')
    search_fields = ('date', 'id')


class BelApbUnAuthAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'usd', 'rur', 'eur')


class BelBankAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'company', 'eur_buy', 'eur_sell', 'usd_buy', 'usd_sell', 'rur_buy', 'rur_sell')
    list_display_links = ('id', 'date')
    search_fields = ('date', 'id')


class BelBankUnAuthAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'usd', 'rur', 'eur')


admin.site.register(Company, CompanyAdmin)
admin.site.register(AlfaBank, AlfaBankAdmin)
admin.site.register(AlfaBankUnAuth, AlfaBankUnAuthAdmin)
admin.site.register(BelApb, BelApbAdmin)
admin.site.register(BelApbUnAuth, BelApbUnAuthAdmin)
admin.site.register(BelBank, BelBankAdmin)
admin.site.register(BelBankUnAuth, BelBankUnAuthAdmin)
