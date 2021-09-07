from django.urls import path
from .views import RegisterFormView, LoginFormView, logout_user

urlpatterns = [
    path('register/', RegisterFormView.as_view()),
    path('login/', LoginFormView.as_view()),
    path('logout/', logout_user),

]
