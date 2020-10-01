from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from bowring.forms.event.newform import NewForm
from bowring.models import Event

@login_required
def new(request):
    form = NewForm()
    return render(request, 'event/new.html', {"form": form})

def create(request):
    print(request.user)
    form = NewForm(request.POST)
    if form.is_valid():
        event = Event(
            name=form.data["name"],
            event_date=form.data["event_date"],
            user=request.user
        )

        event.save(request)
        return redirect("bowring:home")

    return render(request, "event/new.html", {"form": form})