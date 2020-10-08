from django.urls import path

from v1.views.gamescore_view import GameScoreView
from v1.views.framescore_view import FrameScoreView

app_name = "v1"

urlpatterns = [
    path('gamescore/', GameScoreView.as_view(), name='gamescore'),
    path('framescore/', FrameScoreView.as_view(), name='framescore'),
]