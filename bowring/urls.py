from django.urls import path

from .views import homeview, loginview, logoutview, eventview

app_name = "bowring"
urlpatterns = [
    path('login', loginview.index, name='login'),
    path('home', homeview.get, name='home'),
    path('event/new', eventview.new, name='evnet_new'),
    path('logout', logoutview.index, name='logout'),
]