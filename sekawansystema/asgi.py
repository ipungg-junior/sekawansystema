import os
import django
django.setup()
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from apps import urls  # Gantilah dengan rute aplikasi Anda

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sekawansystema.settings')
# settings.configure()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            urls.websocket_urlpatterns
        )
    ),
})
