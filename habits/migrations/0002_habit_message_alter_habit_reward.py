# Generated by Django 4.1.7 on 2023-03-09 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='message',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='habit',
            name='reward',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
