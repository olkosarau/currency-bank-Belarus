from django.urls import path
from .views import AlfaBankViewSet, AlfaBankUnAuthViewSet, BelApbViewSet, BelBankViewSet, BelApbUnAuthViewSet, \
    BelBankUnAuthViewSet

urlpatterns = [

    path('alfabank', AlfaBankViewSet.as_view(), name='alfabank'),
    path('unauchAB', AlfaBankUnAuthViewSet.as_view()),
    path('belagro', BelApbViewSet.as_view(), name='belagrbank'),
    path('unauchBAB', BelApbUnAuthViewSet.as_view()),
    path('belbank', BelBankViewSet.as_view()),
    path('unauchBB', BelBankUnAuthViewSet.as_view()),


]