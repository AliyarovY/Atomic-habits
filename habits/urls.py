from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'private_habits', PrivateHabitViewSet, basename='private_habits')
router.register(r'common_habits', CommonHabitViewSet)

urlpatterns = router.urls
