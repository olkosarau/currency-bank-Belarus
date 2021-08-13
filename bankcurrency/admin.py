from django.contrib import admin
from .models import AlfaBank, AlfaBankUnAuth, BelApb, BelApbUnAuth, BelBank, BelBankUnAuth


class AlfaBankAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'eur_buy', 'eur_sell', 'usd_buy', 'usd_sell', 'rur_buy', 'rur_sell')
    list_display_links = ('id', 'date')
    search_fields = ('date', 'id')


class AlfaBankUnAuthAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'usd', 'rur', 'eur')


class BelApbAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'eur_buy', 'eur_sell', 'usd_buy', 'usd_sell', 'rur_buy', 'rur_sell')
    list_display_links = ('id', 'date')
    search_fields = ('date', 'id')


class BelApbUnAuthAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'usd', 'rur', 'eur')


class BelBankAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'eur_buy', 'eur_sell', 'usd_buy', 'usd_sell', 'rur_buy', 'rur_sell')
    list_display_links = ('id', 'date')
    search_fields = ('date', 'id')


class BelBankUnAuthAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'usd', 'rur', 'eur')


admin.site.register(AlfaBank, AlfaBankAdmin)
admin.site.register(AlfaBankUnAuth, AlfaBankUnAuthAdmin)
admin.site.register(BelApb, BelApbAdmin)
admin.site.register(BelApbUnAuth, BelApbUnAuthAdmin)
admin.site.register(BelBank, BelBankAdmin)
admin.site.register(BelBankUnAuth, BelBankUnAuthAdmin)
