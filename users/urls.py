
from django.urls import path
from django.conf.urls import url, patterns
from .views import RegistrationAPIView, UserRetrieveUpdateAPIView, LoginAPIView

urlpatterns = [
    path('create/', RegistrationAPIView.as_view()),
    path('update/', UserRetrieveUpdateAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
]