from django.urls import path

from v1.views.gamescore_view import GameScoreView

app_name = "v1"

urlpatterns = [
    path('gamescore/', GameScoreView.as_view(), name='gamescore_get'),
]