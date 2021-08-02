
from django.urls import path
from django.conf.urls import url, patterns
from .views import RegistrationAPIView, UserRetrieveUpdateAPIView, LoginAPIView

urlpatterns = [
    path('create/user', RegistrationAPIView.as_view()),
    path('update/user', UserRetrieveUpdateAPIView.as_view()),
    path('user/login/', LoginAPIView.as_view()),
]