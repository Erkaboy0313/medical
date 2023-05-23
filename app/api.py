from rest_framework.routers import DefaultRouter,SimpleRouter
from django.conf import settings
from .views import HomeView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r'home',HomeView,basename='home')
