from django.urls import path
from .views import TaskListView, display_tasks, delete_task, TaskCreateView, TaskDetailView

urlpatterns = [
    path('', TaskListView.as_view(), name='index'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task'),
    path('create_task/', TaskCreateView.as_view(), name='create_task'),
    path('display_tasks/', display_tasks, name='display_tasks'),
    path('task/<int:id>/delete/', delete_task, name='delete_task'),
]
