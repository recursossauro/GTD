from django.urls import path
from tasks.views import (
    TaskListView,
    display_tasks,
    delete_task,
    TaskCreateView,
    TaskUpdateView,
    TaskDetailView,
    conclude_or_not_task, create_history,
)

urlpatterns = [
# TASK
    path('', TaskListView.as_view(), name='index'),
    path('task/create/', TaskCreateView.as_view(), name='create_task'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='update_task'),
    path('display_tasks/', display_tasks, name='display_tasks'),
    path('task/<int:pk>/conclude/', conclude_or_not_task, name='concludeornottask'),
    path('task/<int:id>/delete/', delete_task, name='delete_task'),
# TASK HISTORY
    path('task_history/<int:task_id>/new/', create_history, name='new_task_history'),
]
