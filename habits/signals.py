from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Habit
from config import tasks


@receiver(post_save, sender=Habit)
def habit_telegram_send(sender, instance, created, **kwargs):
    frequency = instance.frequency
    run_time = instance.run_time
    message = instance.message or instance.__str__()
    telegram_id = instance.telegram_id

    tasks.add_telegram.delay(frequency, run_time, telegram_id, message)
