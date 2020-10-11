from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core import error
from bowring.forms.gamescore.newform import NewForm
from bowring.models.events import Event
from bowring.models.gamescores import GameScore

@login_required
def new(request, event_id):

    event = Event.check_event(event_id, request.user)
    if not event:
        return error.handler404(request)

    form = NewForm()
    gamescore = GameScore.nextgame(user=request.user, event=event)
    form.gamescore = gamescore

    return render(request, 'gamescore/new.html', {"form": form})

def edit(request, event_id, game_count):

    event = Event.check_event(event_id, request.user)
    if not event:
        return error.handler404(request)

    gamescore = GameScore.check_score(event=event, game_count=game_count)
    if not gamescore:
        return error.handler404(request)

    form = NewForm()
    form.gamescore = gamescore
    form.fields["event_id"].initial = event.id
    form.fields["gamecount"].initial = game_count

    return render(request, 'gamescore/edit.html', {"form": form})