# Generated by Django 5.1.2 on 2024-11-05 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_dt_scheduled_alter_taskhistory_dt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dt_scheduled',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 11, 12, 13, 11, 46, 727769, tzinfo=datetime.timezone.utc), null=True, verbose_name='Scheduled for'),
        ),
        migrations.AlterField(
            model_name='taskcontrol',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 5, 13, 11, 46, 728230, tzinfo=datetime.timezone.utc), verbose_name='Date'),
        ),
        migrations.DeleteModel(
            name='TaskHistory',
        ),
    ]