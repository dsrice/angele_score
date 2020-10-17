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
    result = models.ForeignKey(Result, on_delete=models.PROTECT, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    frame_count = models.IntegerField()
    frame_score = models.IntegerField()

    class Meta:
        db_table = "frame_scores"

    @staticmethod
    def check_framescore(game_score: GameScore, user: User, frame_count: int):
        """
        frame_scoreの存在確認
        """
        if FrameScore.objects.filter(gamescore=game_score, user=user, frame_count=frame_count).exists():
            return FrameScore.objects.get(gamescore=game_score, user=user, frame_count=frame_count)
        else:
            print("ok")
            return None
