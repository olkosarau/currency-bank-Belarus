from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from users.forms import LoginForm, RegisterUserForm
from .models import User


class RegisterFormView(FormView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    success_url = reverse_lazy('/login')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print('999')
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Вы Зарегистрировались!!!')
                form.save()
                return redirect('/login')
            else:
                print('666666')
        else:
            form = RegisterUserForm()

        context = {'form': form}
        return render(request, 'users/register.html', context)


class LoginFormView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('/company')

    def post(self, request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы Вошли В Систему!')
                return redirect('/company')

            else:
                messages.success(request, 'Ошибка Входа В Систему')
                return redirect('/login')
        else:
            return render(request, 'users/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'Вы Вышли Из Системы')
    return redirect('/company')
