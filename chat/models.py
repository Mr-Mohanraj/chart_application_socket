from django.db import models

class User(models.Model):
    username = models.CharField(max_length=250)
    roomName = models.CharField(max_length=8)
    # RoomUser = models.ManyToManyField('self', verbose_name="room_user", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class RoomUser(models.Model):
#     pass
