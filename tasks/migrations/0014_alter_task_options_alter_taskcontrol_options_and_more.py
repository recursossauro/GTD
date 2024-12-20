# Generated by Django 5.1.2 on 2024-11-29 02:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_taskcontrol_user_alter_task_dt_scheduled_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['user', 'dt_completed', 'dt_scheduled'], 'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterModelOptions(
            name='taskcontrol',
            options={'ordering': ['user', 'task', '-dt'], 'verbose_name': 'Task_Control', 'verbose_name_plural': 'Task_Controls'},
        ),
        migrations.AlterField(
            model_name='task',
            name='dt_scheduled',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 6, 2, 35, 11, 674340, tzinfo=datetime.timezone.utc), null=True, verbose_name='Scheduled for'),
        ),
        migrations.AlterField(
            model_name='taskcontrol',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 29, 2, 35, 11, 675012, tzinfo=datetime.timezone.utc), verbose_name='Date'),
        ),
    ]
