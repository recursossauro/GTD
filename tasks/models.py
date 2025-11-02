from django.db import models
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from datetime import timedelta
from django.conf import settings
from django.db.models import Q

defautlSchedule = now() + timedelta(days=7)

class Task(models.Model):
    # A Task could be a task, a stuff, a project, a reference.
    TYPE_CHOICES = {
        'ST': 'Stuff',
        'TK': 'Task',
        'PJ': 'Project',
        'RF': 'Reference',
    }

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='User', on_delete=models.CASCADE)

    type = models.CharField('Type', max_length=2, choices=TYPE_CHOICES, default='TK')
    title = models.CharField("Title", max_length=160)
    description = models.TextField("description", blank=True, null=True)

    dt_scheduled = models.DateTimeField("Scheduled for", blank=True, null=True, default=defautlSchedule)
    dt_completed = models.DateTimeField("Completed on", blank=True, null=True)
    dt_canceled  = models.DateTimeField("Completed on", blank=True, null=True)

    # Fields to backup control
    created = models.DateTimeField('Created', auto_now_add=True, null=True)
    modified = models.DateTimeField('Modified', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['user', 'dt_completed','dt_scheduled']

    def save(self, *args, **kwargs):

        # Do tests to create history about:
        #   Task Created
        #   Task Completed
        #   Changed date completed.
        #   Task turned uncompleted.


        if not self.pk:
            # Prepare create history for Task Created
            taskControl = TaskControl(task=self, user=self.user, description='Task Created')
        else:
            originalTask = get_object_or_404(Task, pk=self.pk)
            if self.dt_completed:
                if originalTask.dt_completed:
                    if originalTask.dt_completed != self.dt_completed:
                        taskControl = TaskControl(task=self, user=self.user, description='Task completed date was changed.')
                else:
                    taskControl = TaskControl(task=self, user=self.user, description='Task completed.')
            else:
                if originalTask.dt_completed:
                    taskControl = TaskControl(task=self, user=self.user, description='Task returned uncompleted.')


        super(Task, self).save(*args, **kwargs)

        try:
            taskControl.save()
        except NameError:
            pass

    def getHistory(self):
        return self.taskcontrol_set.filter(type='HS').order_by('-dt')

    def getSchedules(self):
        return self.taskcontrol_set.filter(type='SC').order_by('-dt')

    @classmethod
    def getTodayTasks(cls):
        # filter all tasks not completed type task and dt_scheduled is today or has schedule for today.
        return cls.objects.filter(
            Q(taskcontrol__type='SC') & Q(taskcontrol__dt__date=now()) | Q(dt_scheduled__date=now()),
            type='TK',
            dt_completed__isnull=True).distinct()

    def __str__(self):
        return self.title


class TaskControl(models.Model):
    TYPE_CHOICES = {
        'HS':'History',
        'SC':'Schedule', # Schedule to doing
        'DL': 'Dead Line', # Date to finish
    }

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='User', on_delete=models.CASCADE, blank=True,
                             null=True)

    task         = models.ForeignKey(Task, on_delete=models.CASCADE)
    type         = models.CharField('Type', max_length=2, choices=TYPE_CHOICES, default='HS')
    dt           = models.DateTimeField('Date', default=now())
    dt_scheduled = models.DateTimeField('Date', default=now(), blank=True, null=True)
    description  = models.TextField("description")

    # Fields to backup control
    created = models.DateTimeField('Created', auto_now_add=True, null=True)
    modified = models.DateTimeField('Modified', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Task_Control'
        verbose_name_plural = 'Task_Controls'
        ordering = ['user', 'task','-dt']

    def __str__(self):
        return str(self.dt) + ' - ' + self.description[:100]

    def getSchedules(self, FromToday=0):
        day = now() + timedelta(days=FromToday)
        schedules = self.objects.filter(type='SC', dt_scheduled__day = day.day)

        return schedules


