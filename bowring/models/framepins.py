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
    result = models.ForeignKey(Result, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    framescore = models.ForeignKey(FrameScore, on_delete=models.PROTECT)
    pin1 = models.BooleanField()
    pin2 = models.BooleanField()
    pin3 = models.BooleanField()
    pin4 = models.BooleanField()
    pin5 = models.BooleanField()
    pin6 = models.BooleanField()
    pin7 = models.BooleanField()
    pin8 = models.BooleanField()
    pin9 = models.BooleanField()
    pin10 = models.BooleanField()

    class Meta:
        db_table = "frame_pins"