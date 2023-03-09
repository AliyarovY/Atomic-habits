from celery import shared_task
import telebot
from django.conf import settings
from time import sleep


def _send_telegram(telegram_id: int, message: str) -> None:
    bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)
    bot.send_message(telegram_id, message)


@shared_task
def add_telegram(frequency: int, run_time: int, telegram_id: int,
                 message: str) -> None:
    sleep_time = frequency + run_time
    while True:
        _send_telegram(telegram_id, message)
        sleep(sleep_time)
