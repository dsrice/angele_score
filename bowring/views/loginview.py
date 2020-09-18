from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from ..forms.loginform import LoginForm

class Account_login(View):
    """
    ログイン関連
    """
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        return render(request, 'bowring/login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'bowring/login.html', {'form': form,})

