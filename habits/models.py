from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


NULLABLE = dict(null=True, blank=True)


class Habit(models.Model):
    '''Привычка, которую необходимо внедрить или приятная привычка'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=255, **NULLABLE)
    when = models.DateTimeField()
    action = models.CharField(max_length=255)
    related_habit = models.ForeignKey('self',
                                      on_delete=models.SET_NULL,
                                      default=None,
                                      **NULLABLE,
                                      )
    is_enjoyful = models.BooleanField(default=False)
    frequency = models.PositiveIntegerField()
    run_time = models.PositiveIntegerField()
    reward = models.CharField(max_length=255, **NULLABLE)
    is_public = models.BooleanField(default=False)
    telegram_id = models.IntegerField(**NULLABLE)
    message = models.CharField(max_length=255, **NULLABLE)

    def __str__(self):
        return f'Я буду {self.action} в {self.when} в {self.place}.'


    class Meta:
        verbose_name = 'habit'
        verbose_name_plural = 'habits'
        db_table = 'habit'


    def validate_run_time(self):
        if self.run_time > 120:
            raise ValidationError('время выполнения должно быть не больше 120 секунд')

    def validate_reward_related_habit(self):
        if all(x != None for x in [self.reward, self.related_habit]):
            raise ValidationError(' одновременный выбор связанной привычки и указания вознаграждения')
        if all(x is None for x in [self.reward, self.related_habit]):
            raise ValidationError('нельзя, чтобы связанная привычка и вознаграждение были одновременно пустые')

    def validate_relate_habit(self):
        if not self.related_habit is None:
            if not self.related_habit.is_enjoyful:
                raise ValidationError(
                    'в связанные привычки могут попадать только привычки с признаком приятной привычки')

    def validate_is_enjoyful(self):
        if self.is_enjoyful:
            if self.reward or self.related_habit:
                raise ValidationError('у приятной привычки не может быть вознаграждения или связанной привычки')

    def validate_frequency(self):
        if self.frequency > 604_800:
            raise ValidationError(
                'периодичность не может быть более 7 дней, то есть привычку нельзя выполнять больше, чем раз в неделю')

    def save(self, *args, **kwargs):
        self.validate_run_time()
        self.validate_reward_related_habit()
        self.validate_relate_habit()
        self.validate_is_enjoyful()
        self.validate_frequency()

        return super().save(*args, **kwargs)
