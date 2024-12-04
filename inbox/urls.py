from django.urls import path
from inbox.views import (
    StuffCreateView,
    StuffListView,
    IndexTemplateView,
    delete_stuff,
    display_stuffs,
)

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('stuff/create/', StuffCreateView.as_view(), name='create_stuff'),
    path('stuff/list/', display_stuffs, name='stuffs'),
    path('stuff/<int:pk>/delete/', delete_stuff, name='delete_stuff'),
]