from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required

from bowring.forms.homeform import  HomeForm
from django.contrib.auth import login, authenticate

@login_required
def get(request):
    form = HomeForm()

    form.events=form.events.filter(user=request.user)
    return render(request, 'home/index.html', {'form': form})
