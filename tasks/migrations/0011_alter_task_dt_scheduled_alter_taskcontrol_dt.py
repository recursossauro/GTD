# Generated by Django 5.1.2 on 2024-11-21 00:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_alter_task_dt_scheduled_alter_taskcontrol_dt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dt_scheduled',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 11, 28, 0, 9, 45, 420945, tzinfo=datetime.timezone.utc), null=True, verbose_name='Scheduled for'),
        ),
        migrations.AlterField(
            model_name='taskcontrol',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 21, 0, 9, 45, 421496, tzinfo=datetime.timezone.utc), verbose_name='Date'),
        ),
    ]
