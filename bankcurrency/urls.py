from django.urls import path
from .views import AuthViewSet, UnAuthViewSet

urlpatterns = [

    path('alfabank', AuthViewSet.alfa_bank),
    path('belagro', AuthViewSet.bel_agro),
    path('belbank', AuthViewSet.belarus_bank),
    path('alfabankUn', UnAuthViewSet.alfa_bank),
    path('belagroUn', UnAuthViewSet.bel_agro),
    path('belbankUn', UnAuthViewSet.belarus_bank),
    path('datecurrent', AuthViewSet.data_date_current),
    path('dateinterval', AuthViewSet.data_date_interval),


]