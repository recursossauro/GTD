# Generated by Django 5.1.2 on 2024-11-05 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_dt_scheduled_taskhistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['dt_completed', 'dt_scheduled'], 'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterField(
            model_name='task',
            name='dt_completed',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Completed on'),
        ),
        migrations.AlterField(
            model_name='task',
            name='dt_scheduled',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 11, 12, 13, 7, 48, 938880, tzinfo=datetime.timezone.utc), null=True, verbose_name='Scheduled for'),
        ),
        migrations.AlterField(
            model_name='taskhistory',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 5, 13, 7, 48, 939432, tzinfo=datetime.timezone.utc), verbose_name='Date'),
        ),
    ]