from django.urls import path

from .views.indexview import Index
from .views.loginview import Account_login

urlpatterns = [
    path('', Index.index, name='index'),
    path('login', Account_login.as_view(), name='login'),
]