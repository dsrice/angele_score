from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core import error
from bowring.forms.gamescore.newform import NewForm
from bowring.models.events import Event

@login_required
def new(request, event_id):

    event = Event.check_event(event_id, request.user)
    if not event:
        return error.handler404(request)

    form = NewForm()



    return render(request, 'gamescore/new.html')

