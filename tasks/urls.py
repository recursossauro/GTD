from django.urls import path
from tasks.views import (
    TaskListView,
    display_tasks,
    delete_task,
    TaskCreateView,
    TaskUpdateView,
    TaskDetailView,
    conclude_or_not_task,
    task_conclude,
    create_history,
    delete_TaskControl,
    display_task_history,
    create_task_schedule,
    display_task_schedule,
)


urlpatterns = [
# TASK
    path('', TaskListView.as_view(), name='index'),
    path('task/create/', TaskCreateView.as_view(), name='create_task'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='update_task'),
    path('task/<int:pk>/from_inbox/', TaskDetailView.as_view(), name='from_inbox'),
    path('display_tasks/', display_tasks, name='display_tasks'),
    path('task/<int:pk>/conclude/', task_conclude, name='conclude_task'),
    path('task/<int:pk>/concludeornot/', conclude_or_not_task, name='concludeornottask'),
    path('task/<int:id>/delete/', delete_task, name='delete_task'),
# TASK HISTORY
    path('task_history/<int:task_id>/new/', create_history, name='new_task_history'),
    path('display_task_history/<int:task_id>/', display_task_history, name='display_task_history'),
    path('task_control/<int:task_id>/<int:id>/delete/', delete_TaskControl, name='delete_task_control'),
# TASK SCHEDULE
    path('task_schedule/<int:task_pk>/new/', create_task_schedule, name='new_task_schedule'),
    path('task_schedule/<int:task_pk>/new/deadline', create_task_schedule, name='new_deadline'),
    path('display_task_shcedule/<int:task_id>/', display_task_schedule, name='display_task_schedule'),
]
