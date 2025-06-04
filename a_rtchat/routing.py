from django.urls import path
from .comsumers import *

websocket_urlpatters = [
    path("ws/chatroom/<chatroom_name>",ChatroomComsumer.as_asgi()),
]