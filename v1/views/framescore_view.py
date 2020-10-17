from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from v1.serializers.framescore import FrameScoreSerializer
from bowring.models.events import Event
from bowring.models.gamescores import GameScore
from bowring.models.framescores import FrameScore
from bowring.models.framepins import FramePin

class FrameScoreView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            params = FrameScoreSerializer(data=request.data)
            if not params.is_valid():
                print(request.data)
                return Response(params.errors, status.HTTP_400_BAD_REQUEST)

            event = Event.check_event(params.data["event_id"], request.user)

            if not event:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            gama_score = GameScore.check_score(event=event, game_count=params.data["game_count"])
            if not gama_score:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            frame_score = FrameScore.check_score(game_score=gama_score, user=request.user, frame_count=params.data["frame_count"])
            if not frame_score:
                frame_score = FrameScore(
                    gamescore=gama_score,
                    user=request.user,
                    frame_count=params.data["frame_count"],
                    result=gama_score.result,
                    frame_score=0,
                    frame_type=1
                )
                frame_score.save()






            result = {}
            return Response(result)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
