from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', required=True, max_length=32)
    email = forms.EmailField(label='Email', required=True, max_length=32, )
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())