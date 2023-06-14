from django.urls import re_path

from . import consumers
print("before the routing")
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<user_name>\w+)/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi(), name="room_route"),
]