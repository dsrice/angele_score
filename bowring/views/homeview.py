from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required

from bowring.forms.homeform import  HomeForm
from django.contrib.auth import login, authenticate

@login_required
def get(request):
    print(request.user)
    form = HomeForm()
    return render(request, 'bowring/home.html', {'form': form })
