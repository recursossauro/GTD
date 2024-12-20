# Generated by Django 5.1.2 on 2024-11-05 13:08

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_task_options_alter_task_dt_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dt_scheduled',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 11, 12, 13, 8, 36, 24623, tzinfo=datetime.timezone.utc), null=True, verbose_name='Scheduled for'),
        ),
        migrations.AlterField(
            model_name='taskhistory',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 5, 13, 8, 36, 25536, tzinfo=datetime.timezone.utc), verbose_name='Date'),
        ),
        migrations.CreateModel(
            name='TaskControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=datetime.datetime(2024, 11, 5, 13, 8, 36, 25100, tzinfo=datetime.timezone.utc), verbose_name='Date')),
                ('description', models.TextField(verbose_name='description')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Modified')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
            options={
                'verbose_name': 'Task_Control',
                'verbose_name_plural': 'Task_Controls',
                'ordering': ['task', '-dt'],
            },
        ),
    ]
