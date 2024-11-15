# Generated by Django 5.1.2 on 2024-11-15 01:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_taskcontrol_type_alter_task_dt_scheduled_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dt_scheduled',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 11, 22, 1, 8, 58, 386885, tzinfo=datetime.timezone.utc), null=True, verbose_name='Scheduled for'),
        ),
        migrations.AlterField(
            model_name='taskcontrol',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 15, 1, 8, 58, 387494, tzinfo=datetime.timezone.utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='taskcontrol',
            name='type',
            field=models.CharField(choices=[('HS', 'History'), ('SC', 'Schedule')], default='HS', max_length=2, verbose_name='Type'),
        ),
    ]
