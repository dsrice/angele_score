from django.db import models
from core.models import TimeStampedModel

from bowring.models.users import User
from bowring.models.results import Result
from bowring.models.gamescores import GameScore

class FrameScore(TimeStampedModel):
    """
    フレームスコア情報
    """
    gamescore = models.ForeignKey(GameScore, on_delete=models.PROTECT)
    result = models.ForeignKey(Result, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    frame_count = models.IntegerField()
    frame_type = models.IntegerField()
    frame_score = models.IntegerField()

    class Meta:
        db_table = "frame_scores"

