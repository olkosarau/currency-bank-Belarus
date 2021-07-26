from django.contrib import admin
from .models import AlfaBank


class AlfaBankAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'usd', 'rur','eur', 'date', 'done')  # ие поля мы будем видеть в списке
    list_display_links = ('id', 'title')
    search_fields = ('date', 'id')  # по каким полям мы можем искать
    list_filter = ('done',)


admin.site.register(AlfaBank, AlfaBankAdmin)
