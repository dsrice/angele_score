from django.urls import path

from .views import homeview, loginview, logoutview

app_name = "bowring"
urlpatterns = [
    path('login', loginview.index, name='login'),
    path('home', homeview.get, name='home'),
    path('logout', logoutview.index, name='logout'),
]