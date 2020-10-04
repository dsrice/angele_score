from django.urls import path

from .views import homeview, loginview, logoutview, eventview

app_name = "bowring"
urlpatterns = [
    path('login', loginview.index, name='login'),
    path('home', homeview.get, name='home'),
    path('event/new', eventview.new, name='evnet_new'),
    path('event/create', eventview.create, name='evnet_create'),
    path('event/<int:event_id>/show', eventview.show, name='evnet_show'),
    path('logout', logoutview.index, name='logout'),
]