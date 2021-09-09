from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from users.forms import RegisterUserForm


class RegisterFormView(FormView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    success_url = '/auth/login/'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return super(RegisterFormView, self).form_valid(form)


class LoginFormView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('/company/rates/')

    def validars(request):
        if request.user.is_authenticated():
            if request.user.is_staff:
                return messages.success(request, 'Вы вошли')

        return redirect('/auth/login/')


def logout_user(request):
    logout(request)
    messages.success(request, 'Вы Вышли Из Системы')
    return redirect('/company/sellrates/')
