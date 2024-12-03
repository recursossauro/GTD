from django.urls import path
from tasks.views import (
    TaskCreateView,
    display_tasks,
)
from inbox.views import (
    StuffCreateView,
    StuffListView, IndexTemplateView,
)

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('stuff/create/', StuffCreateView.as_view(), name='create_stuff'),
    path('stuff/list/', StuffListView.as_view(), name='stuffs'),
]