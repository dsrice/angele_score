from django.db import models



class TimeStampedModel(models.Model):
    """
    抽象基底クラス
    """

    created_at = models.DateTimeField(auto_now_add=True)
    created_user_id = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_user_id = models.IntegerField()
    is_deleted = models.IntegerField(default=0)
    deleted_at = models.DateTimeField()
    deleted_user_id = models.IntegerField()

    class Meta:
        abstract = True