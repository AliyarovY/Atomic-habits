from django.urls import path, include
from rest_framework import routers

from .views import UserCreateView


router = routers.DefaultRouter()
router.register(r'registration', UserCreateView)

urlpatterns = [
    path('', include(router.urls)),
]
