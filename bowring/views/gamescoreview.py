from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from bowring.forms.event.newform import NewForm
from bowring.forms.event.showform import ShowForm
from bowring.models.events import Event


@login_required
def new(request):
    return render(request, 'gamescore/new.html')

