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

            user = request.user
            event = Event.check_event(params.data["event_id"], request.user)

            if not event:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            gama_score = GameScore.check_score(event=event, game_count=params.data["game_count"])
            if not gama_score:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            frame_score = FrameScore.check_framescore(game_score=gama_score, user=user, frame_count=params.data["frame_count"])
            if not frame_score:
                frame_score = FrameScore(
                    gamescore=gama_score,
                    user=user,
                    frame_count=params.data["frame_count"],
                    frame_score=0
                )
                frame_score.save(user)

            frame_pin = FramePin.check_pin(game_score=gama_score, user=user, frame_score=frame_score, throw_count=params.data["throw_count"])
            if not frame_pin:
                frame_pin = FramePin(
                    gamescore=gama_score,
                    user=user,
                    framescore=frame_score,
                    throw_count=params.data["throw_count"],
                    pin1=0,
                    pin2=0,
                    pin3=0,
                    pin4=0,
                    pin5=0,
                    pin6=0,
                    pin7=0,
                    pin8=0,
                    pin9=0,
                    pin10=0
                )
                frame_pin.save(user)

            print(frame_pin)
            frame_pin = self.__update_pin(pins=params.data["pins"], frame_pin=frame_pin)
            frame_pin.save(user)


            result = {}
            return Response(result)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def __update_pin(self, pins: list, frame_pin: FramePin):
        """
        ピン情報の更新
        """
        frame_pin.pin1 = pins[0]
        frame_pin.pin2 = pins[1]
        frame_pin.pin3 = pins[2]
        frame_pin.pin4 = pins[3]
        frame_pin.pin5 = pins[4]
        frame_pin.pin6 = pins[5]
        frame_pin.pin7 = pins[6]
        frame_pin.pin8 = pins[7]
        frame_pin.pin9 = pins[8]
        frame_pin.pin10 = pins[9]

        return frame_pin
