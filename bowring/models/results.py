from django.db import models
from core.models import TimeStampedModel
from bowring.models.events import Event
from bowring.models.users import User

class Result(TimeStampedModel):
    """
    スコア概要情報
    """
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    total_score = models.IntegerField()
    base_score = models.IntegerField()
    total_handicap = models.IntegerField()

    class Meta:
        db_table = "results"

