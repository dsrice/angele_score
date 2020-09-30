from django.shortcuts import render, redirect
from django.views import View

from bowring.forms.loginform import LoginForm
from django.contrib.auth import login, authenticate


def index(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user = authenticate(email=form.data["email"], password=form.data["password"])
        if user:
            login(request, user)
            return redirect("bowring:home")

    return render(request, 'login/index.html', {'form': form})
