# Generated by Django 4.1.7 on 2023-03-09 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=255, null=True)),
                ('when', models.DateTimeField()),
                ('action', models.CharField(max_length=255)),
                ('is_enjoyful', models.BooleanField(default=False)),
                ('frequency', models.PositiveIntegerField()),
                ('run_time', models.PositiveIntegerField()),
                ('reward', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('is_public', models.BooleanField(default=False)),
                ('telegram_id', models.IntegerField(blank=True, null=True)),
                ('related_habit', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'habit',
                'verbose_name_plural': 'habits',
                'db_table': 'habit',
            },
        ),
    ]
