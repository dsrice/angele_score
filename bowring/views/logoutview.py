from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

@login_required
def index(request):
    logout(request)
    return redirect("bowring:login")
