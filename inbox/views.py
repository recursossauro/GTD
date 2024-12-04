from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render
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

@login_required
def display_stuffs(request):

    context = {
            'object_list': Task.objects.filter(user=request.user, type='ST'),
    }

    return render(request, 'inbox/stuff_list.html', context)

@login_required
@require_http_methods(['DELETE'])
def delete_stuff(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user, type="ST")
    task.delete()
    return HttpResponseRedirect(reverse("inbox:stuffs"))