from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from core.models import TimeStampedModel

from bowring.models.users import User

class Event(TimeStampedModel):
    """
    イベント情報
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    event_date = models.DateTimeField()
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "events"

    def check_event(event_id, user):
        """
        対象のイベントとユーザのセットが成立しているかの確認
        """
        event = Event.objects.filter(id=event_id, user=user)
        if event:
            return event[0]
        return None
