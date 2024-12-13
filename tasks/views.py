from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request
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

    def form_valid(self, form: object) -> object:
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'tasks/update_task.html'
    model = Task
    fields = ['title', 'description', 'dt_scheduled', 'dt_completed']

    def get_success_url(self):
        #   print(self.request.GET.get('next', reverse_lazy('tasks:task', kwargs={'pk': self.object.pk})))
        return self.request.GET.get('next', reverse_lazy('tasks:task', kwargs={'pk': self.object.pk}))

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # Check if the logged user is the Task creator.
        if obj.user != self.request.user:
            raise PermissionDenied("You has no permission to edit this Task.")
        return obj


@login_required
def display_tasks(request):

    context = {
        'tasks': {
            'uncompleted_tasks': Task.objects.filter(dt_completed__isnull=True, user=request.user, type='TK'),
            'completed_tasks': Task.objects.filter(dt_completed__isnull=False, user=request.user, type='TK'),
        }
    }

    return render(request, 'tasks/task_list.html', context)

class TaskDetailView(LoginRequiredMixin, DetailView):
    template_name = "tasks/task.html"
    model = Task

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # Check if the logged user is the Task creator.
        if obj.user != self.request.user:
            raise PermissionDenied("You has no permission to access this Task.")
        # Check if the path has from_inbox and task is a stuff
        if 'from_inbox' in self.request.path and obj.type == 'ST':
            obj.type = 'TK'
            obj.save()
        return obj


class TaskListView(LoginRequiredMixin, ListView):
    template_name = 'tasks/index.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user, type='TK')

@login_required
@require_http_methods(['DELETE'])
def delete_task(request, id):
    Task.objects.filter(id=id, user=request.user).delete()
    return HttpResponseRedirect(reverse("tasks:display_tasks"))

@login_required
def task_conclude(request, pk):

    task = get_object_or_404(Task, pk=pk)
    # Test if user has permission
    if request.user == task.user:
        if task.dt_completed is None:
            task.dt_completed = now()
            task.save()

    if request.GET.get('next') is not None:
        return HttpResponseRedirect(request.GET.get('next'))

    return HttpResponseRedirect(reverse('tasks:task', kwargs={'pk':pk}))

@login_required
def conclude_or_not_task(request, pk):

    # IMPLEMENTAÇÕES FUTURAS:
    #     Verificar se existe POST['checkbox']
    #     Se não houver subir o erro: campo 'checkbox' não foi enviado.

    task = get_object_or_404(Task, pk=pk)

    # Test if user has permission
    if request.user == task.user:
        if ('checkbox' in request.POST):
            if request.POST['checkbox'] == 'checked':
                if task.dt_completed is None:
                    task.dt_completed = now()
                    task.save()
        else:
            if task.dt_completed:
                task.dt_completed = None
                task.save()
    if request.GET.get('next') is not None:
        return HttpResponseRedirect(request.GET.get('next'))
    return HttpResponseRedirect(reverse("tasks:display_tasks"))

# HISTORY

@login_required
def create_history(request, task_id):

    task = Task(id=task_id)

    date = request.POST.get('dt')

    if date is None or date== '':
        TaskControl(user=request.user, task=task, type='HS', description=request.POST.get('description')).save()
    else:
        if 'time' in request.POST and request.POST.get('time'):
            date = date + ' ' + request.POST.get('time')

        TaskControl(ser=request.user, task=task, type='HS', dt=date, description=request.POST.get('description')).save()


    return HttpResponseRedirect(reverse("tasks:task", kwargs={'pk': task_id}))


@login_required
def display_task_history(request, task_id):

    context = {
        'object':Task(id=task_id, user=request.user),
        'histories': TaskControl.objects.filter(task_id = task_id, type='HS', user=request.user).order_by('-dt')
    }

    return render(request, 'tasks/history_list.html', context)

@login_required
@require_http_methods(['DELETE'])
def delete_TaskControl(request, task_id, id):
    TaskControl.objects.filter(id=id).delete()

    if request.GET.get('type') == 'schedule':
        return HttpResponseRedirect(reverse("tasks:display_task_schedule", kwargs={"task_id": task_id}))
    return HttpResponseRedirect(reverse("tasks:display_task_history", kwargs={"task_id": task_id}))


# Task Schedule

@login_required
def display_task_schedule(request, task_id):

    context = {
        'object':Task(id=task_id, user=request.user),
    }

    return render(request, 'tasks/schedule_list.html', context)


@login_required
def create_task_schedule(request, task_pk):
    # Test if exists task pk for the current user
    task = get_object_or_404(Task, pk=task_pk, user=request.user)
    kwargs = {
        'task':task,
        'user':request.user,
        'type':type,
        'description':request.POST.get('description')
    }
    if 'deadline' in request.path:
        kwargs['type'] = 'DL'
    else:
        kwargs['type'] = 'SC'

    if request.POST.get('dt'):
        kwargs['dt'] = request.POST.get('dt')

    TaskControl(**kwargs).save()

    #return HttpResponse('Task ' + str(task) + " scheduled to " + request.POST.get('dt'))
    #return HttpResponseRedirect(reverse("tasks:display_task_schedule", kwargs={"task_id": task_pk}))
    return render(request=request, template_name='tasks/create_schedule.html', context={'object':task, 'schedule_create_message':'Task ' + str(task) + " scheduled to " + request.POST.get('dt')})
