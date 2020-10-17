from rest_framework import serializers

class FrameScoreSerializer(serializers.Serializer):
    """
    framescore用のシリアライザー
    """
    event_id = serializers.IntegerField()
    game_count = serializers.IntegerField()
    frame_count = serializers.IntegerField()
    throw_count = serializers.IntegerField()
    pins = serializers.ListField(
        child=serializers.IntegerField(min_value=0)
    )

