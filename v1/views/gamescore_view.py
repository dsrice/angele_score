from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from bowring.models import Event, GameScore, FrameScore


class GameScoreView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            event_id = request.GET.get("event_id")
            event = Event.check_event(event_id=event_id, user=request.user)
            if not event:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            gamecount = request.GET.get("game_count")
            gamescore = GameScore.check_score(event=event, game_count=gamecount)
            if not gamescore:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            result = {
                "base_score": gamescore.base_score,
                "score": gamescore.score,
                "frames": []
            }
            return Response(result)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
