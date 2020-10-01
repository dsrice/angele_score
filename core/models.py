from django.db import models



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


    def save(self, request=None, **kwargs):
        if request.user.is_authenticated:
            self.updated_user_id = request.user.id
            if not self.created_at:
                self.created_user_id = request.user.id

        super(TimeStampedModel, self).save(**kwargs)