from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    """
    抽象基底クラス
    """

    created_at = models.DateTimeField(auto_now_add=True)
    created_user_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_user_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField(default=0)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, user=None, **kwargs):
        if user and user.is_authenticated:
            self.updated_user_id = user.id
            if not self.created_at:
                self.created_user_id = user.id

        self.updated_at = timezone.now()
        super(TimeStampedModel, self).save(**kwargs)
