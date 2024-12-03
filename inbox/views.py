from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView

from tasks.models import Task

class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'inbox/index.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user, type='ST')

class StuffCreateView(LoginRequiredMixin, CreateView):
    template_name = 'inbox/create_stuff.html'
    model = Task
    fields = ['title']
    success_url = reverse_lazy('inbox:create_stuff')

    def form_valid(self, form: object) -> object:
        form.instance.user = self.request.user
        form.instance.type = 'ST'

        return super().form_valid(form)


class StuffListView(LoginRequiredMixin, ListView):
    template_name = 'inbox/stuff_list.html'
    model = Task


    def get_queryset(self):

        return Task.objects.filter(user=self.request.user, type='ST')