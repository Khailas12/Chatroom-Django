import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

application = get_asgi_application()


"""
import os
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from chat.consumers import ChatRoomConsumer
from django.conf.urls import url


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),

    'websocket': AuthMiddlewareStack(
        URLRouter([
            url(r'ws/chat/(?P<room_name>\w+)/$', ChatRoomConsumer.as_asgi()),
        ])
    ),
})
"""