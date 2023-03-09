from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .serializers import UserSerializer


class UserCreateView(mixins.CreateModelMixin,
                     GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
