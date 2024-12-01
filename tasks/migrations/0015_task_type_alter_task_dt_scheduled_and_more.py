# Generated by Django 5.1.2 on 2024-11-29 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_alter_task_options_alter_taskcontrol_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.CharField(choices=[('ST', 'Stuff'), ('TK', 'Task'), ('PJ', 'Project'), ('RF', 'Reference')], default='TK', max_length=2, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='task',
            name='dt_scheduled',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 6, 12, 36, 57, 594348, tzinfo=datetime.timezone.utc), null=True, verbose_name='Scheduled for'),
        ),
        migrations.AlterField(
            model_name='taskcontrol',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 29, 12, 36, 57, 595312, tzinfo=datetime.timezone.utc), verbose_name='Date'),
        ),
    ]