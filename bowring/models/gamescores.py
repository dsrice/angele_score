from django.db import models
from core.models import TimeStampedModel

from bowring.models.users import User
from bowring.models.results import Result

class GameScore(TimeStampedModel):
    """
    ゲームスコア情報
    """
    result = models.ForeignKey(Result, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    game_count = models.IntegerField()
    score = models.IntegerField()
    base_score = models.IntegerField()
    handicap = models.IntegerField()

    class Meta:
        db_table = "game_scores"

