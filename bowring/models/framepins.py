from django.db import models
from core.models import TimeStampedModel

from bowring.models.users import User
from bowring.models.results import Result
from bowring.models.gamescores import GameScore
from bowring.models.framescores import FrameScore

class FramePin(TimeStampedModel):
    """
    フレームピン情報
    """
    gamescore = models.ForeignKey(GameScore, on_delete=models.PROTECT)
    result = models.ForeignKey(Result, on_delete=models.PROTECT, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    framescore = models.ForeignKey(FrameScore, on_delete=models.PROTECT)
    throw_count = models.IntegerField()
    pin1 = models.IntegerField()
    pin2 = models.IntegerField()
    pin3 = models.IntegerField()
    pin4 = models.IntegerField()
    pin5 = models.IntegerField()
    pin6 = models.IntegerField()
    pin7 = models.IntegerField()
    pin8 = models.IntegerField()
    pin9 = models.IntegerField()
    pin10 = models.IntegerField()

    class Meta:
        db_table = "frame_pins"

    @staticmethod
    def check_pin(game_score: GameScore, user: User, frame_score: FrameScore, throw_count):
        """
        frame_scoreの存在確認
        """
        if FramePin.objects.filter(gamescore=game_score, user=user, framescore=frame_score, throw_count=throw_count).exists():
            return FramePin.objects.get(gamescore=game_score, user=user, framescore=frame_score, throw_count=throw_count)
        else:
            return None