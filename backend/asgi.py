from django.core.asgi import get_asgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
import chat.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket":
        AuthMiddlewareStack(
            AllowedHostsOriginValidator(
                URLRouter(
                    chat.routing.websocket_urlpatterns
                )
            ),
        ),
})
