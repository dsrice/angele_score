from django.urls import path

from .views import homeview, loginview

app_name = "bowring"
urlpatterns = [
    path('login', loginview.index, name='login'),
    path('home', homeview.get, name='home'),
]