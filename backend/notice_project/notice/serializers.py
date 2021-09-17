from django.utils import timezone
from rest_framework import serializers
from django.utils import timezone


class NoticeboardRoom(serializers.Serializer):
    room_id = serializers.UUIDField()
    title = serializers.CharField()
    unread = serializers.IntegerField()
    members = serializers.IntegerField()
    icon = serializers.URLField()
    action = serializers.CharField()


class CreateNoticeSerializer(serializers.Serializer):
<<<<<<< HEAD
    title = serializers.CharField(max_length=255)
    created = serializers.DateTimeField(default_timezone=timezone.now())
    message = serializers.CharField(max_length=255)
=======
    title = serializers.CharField(max_length = 255)
    created = serializers.DateTimeField(default=timezone.now())
    message = serializers.CharField(max_length = 255)
>>>>>>> 6cbf2fe9eaab7590c14a24ade09285f4a5659552
