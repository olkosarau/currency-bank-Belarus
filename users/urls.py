
from django.urls import path
from django.conf.urls import url, patterns
from .views import RegistrationAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    path('create/', RegistrationAPIView.as_view()),
    path('update/', UserRetrieveUpdateAPIView.as_view()),
]