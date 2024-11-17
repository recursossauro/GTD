from django.db import models
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from datetime import timedelta

defautlSchedule = now() + timedelta(days=7)


class Task(models.Model):
    # A Task could be a task, a stuff or a project.

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
        ordering = ['dt_completed','dt_scheduled']

    def save(self, *args, **kwargs):

        # Do tests to create history about:
        #   Task Created
        #   Task Completed
        #   Changed date completed.


        if not self.pk:
            # Prepare create history for Task Created
            taskControl = TaskControl(task=self, description='Task Created')
        elif self.dt_completed:
            originalTask = get_object_or_404(Task, pk = self.pk)
            if originalTask.dt_completed:
                if originalTask.dt_completed != self.dt_completed:
                    taskControl = TaskControl(task=self, description='Task completed date was changed.')
            else:
                taskControl = TaskControl(task=self, description='Task completed.')

        super(Task, self).save(*args, **kwargs)

        try:
            taskControl.save()
        except NameError:
            pass

    def getHistory(self):
        return self.taskcontrol_set.filter(type='HS').order_by('-dt')

    def __str__(self):
        return self.title

class TaskControl(models.Model):
    TYPE_CHOICES = {
        'HS':'History',
        'SC':'Schedule',
    }

    task        = models.ForeignKey(Task, on_delete=models.CASCADE)
    type        = models.CharField('Type', max_length=2, choices=TYPE_CHOICES, default='HS')
    dt          = models.DateTimeField('Date', default=now())
    description = models.TextField("description")

    # Fields to backup control
    created = models.DateTimeField('Created', auto_now_add=True, null=True)
    modified = models.DateTimeField('Modified', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Task_Control'
        verbose_name_plural = 'Task_Controls'
        ordering = ['task','-dt']

    def __str__(self):
        return str(self.dt) + ' - ' + self.description[:100]

