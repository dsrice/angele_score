from django.db import models
from core.models import TimeStampedModel

from bowring.models.users import User
from bowring.models.results import Result
from bowring.models.events import Event


class GameScore(TimeStampedModel):
    """
    ゲームスコア情報
    """
    result = models.ForeignKey(Result, on_delete=models.PROTECT, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    game_count = models.IntegerField()
    score = models.IntegerField(null=True, blank=True)
    base_score = models.IntegerField(null=True, blank=True)
    handicap = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "game_scores"

    @staticmethod
    def nextgame(user: User, event: Event):
        """
        次のゲームの用意
        """
        games = GameScore.objects.filter(event_id=event.id)
        if games:
            count = len(games) + 1
        else:
            count = 1

        newgame = GameScore(
            event=event,
            user=user,
            game_count=count
        )
        newgame.save(user=user)

        return newgame

    @staticmethod
    def check_score(event: Event, game_count: int):
        """
        スコアの存在確認
        """
        if GameScore.objects.filter(event=event, game_count=game_count).exists():
            return GameScore.objects.get(event=event, game_count=game_count)
        else:
            return None
