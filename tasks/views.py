from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.utils.timezone import now
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Task, TaskControl


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'tasks/create_task.html'
    model = Task
    fields = ['title']
    success_url = reverse_lazy('tasks:create_task')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Task.objects.all()

        return context

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'tasks/update_task.html'
    model = Task
    fields = ['title', 'description', 'dt_scheduled', 'dt_completed']

    def get_success_url(self):
        #   print(self.request.GET.get('next', reverse_lazy('tasks:task', kwargs={'pk': self.object.pk})))
        return self.request.GET.get('next', reverse_lazy('tasks:task', kwargs={'pk': self.object.pk}))

@login_required
def display_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'object_list': tasks})

class TaskDetailView(LoginRequiredMixin, DetailView):
    template_name = "tasks/task.html"
    model = Task

class TaskListView(LoginRequiredMixin, ListView):
    template_name = 'tasks/index.html'
    model = Task

@login_required
@require_http_methods(['DELETE'])
def delete_task(request, id):
    Task.objects.filter(id=id).delete()
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'object_list': tasks})

@login_required
def conclude_or_not_task(request, pk):

    # IMPLEMENTAÇÕES FUTURAS:
    #     Verificar se existe POST['checkbox']
    #     Se não houver subir o erro: campo 'checkbox' não foi enviado.

    task = get_object_or_404(Task, pk=pk)
    if ('checkbox' in request.POST):
        if request.POST['checkbox'] == 'checked':
            if task.dt_completed is None:
                task.dt_completed = now()
                task.save()
    else:
        if task.dt_completed:
            task.dt_completed = None
            task.save()

    return HttpResponseRedirect(reverse("tasks:display_tasks"))

@login_required
def create_history(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    date = request.POST.get('dt')
    if 'time' in request.POST:
        date = date + ' ' + request.POST.get('time')

    if date is None or date== '':
        date = now()

    TaskControl(task=task, type='HS', dt=date, description=request.POST.get('description')).save()

    return HttpResponseRedirect(reverse("tasks:task", kwargs={'pk': task_id}))