from django.utils import timezone
from rest_framework import serializers
from .storage import db

<<<<<<< HEAD

class CreateNoticeSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    department = serializers.CharField(max_length=255)
    message = serializers.CharField(max_length=255)
=======
class NoticeboardRoom(serializers.Serializer):
    room_id = serializers.UUIDField()
    title = serializers.CharField()
    unread = serializers.IntegerField()
    members = serializers.IntegerField()
    icon = serializers.URLField()
    action = serializers.CharField()

class CreateNoticeSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 255)
    created = serializers.DateTimeField(default_timezone=timezone.now())
    message = serializers.CharField(max_length = 255)
>>>>>>> 1a859a53a498550d1f4a5b9b770414dea004d3d1
