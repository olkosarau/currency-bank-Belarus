from django.urls import path
from .views import bank

urlpatterns = [
    path('', bank),

]