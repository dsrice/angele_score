from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

class Index():
    def index(request):
        context = {}
        return render(request, "bowring/login.html")
