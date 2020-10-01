from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from bowring.forms.event.newform import NewForm

@login_required
def new(request):
    form = NewForm()
    return render(request, 'event/new.html', {"form": form})
