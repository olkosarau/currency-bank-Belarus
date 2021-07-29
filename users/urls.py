
from django.urls import path
from django.conf.urls import url, patterns
from .views import CreateUserAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('update/', UserRetrieveUpdateAPIView.as_view()),
]