from django.shortcuts import render, redirect
from django.views import View

from bowring.forms.loginform import LoginForm
from django.contrib.auth import login, authenticate
from core.api import Api_method
from core import error


def index(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user = authenticate(email=form.data["email"], password=form.data["password"])
        if user:
            login(request, user)
            api = Api_method()
            token = api.auth(email=form.data["email"], password=form.data["password"])
            if not token:
                return error.handler404(request)

            request.session["token"] = token

            return redirect("bowring:home")

    return render(request, 'login/index.html', {'form': form})
