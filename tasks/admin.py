from django.contrib import admin
from .models import Task, TaskControl

admin.site.register(Task)
admin.site.register(TaskControl)