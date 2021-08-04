
from django.urls import path
from . import views


urlpatterns = [
    path('register', views.RegisterFormView.as_view(), name='register'),
    path('logout', views.logout_user, name='logout'),
    path('login', views.LoginFormView.as_view(), name='login'),

]