from django.urls import path
from .views import RegisterFormView, LoginFormView

urlpatterns = [
    path('register/', RegisterFormView.as_view()),
    path('login/', LoginFormView.as_view()),

]
