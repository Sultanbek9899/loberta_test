from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import FormView
from django.contrib import messages

# Create your views here.
from .forms import LoginForm


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                messages.success(self.request, "You successfully loged in")
                return redirect('index')
            else:
                return HttpResponse("Ваш аккаунт неактивен")
        return HttpResponse("Такого юзера не существует")


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')