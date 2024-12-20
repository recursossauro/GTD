# Generated by Django 5.1.2 on 2024-11-06 23:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_task_dt_scheduled_alter_taskcontrol_dt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='dt_canceled',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Completed on'),
        ),
        migrations.AlterField(
            model_name='task',
            name='dt_scheduled',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 11, 13, 23, 7, 22, 781753, tzinfo=datetime.timezone.utc), null=True, verbose_name='Scheduled for'),
        ),
        migrations.AlterField(
            model_name='taskcontrol',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 6, 23, 7, 22, 782256, tzinfo=datetime.timezone.utc), verbose_name='Date'),
        ),
    ]
