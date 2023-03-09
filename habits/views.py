from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Habit
from .serializers import HabitSerializer


class PrivateHabitViewSet(ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class CommonHabitViewSet(ReadOnlyModelViewSet):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
