from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from task.constants import TASK_COMPLETED
from task.filters import TaskFilter

from task.forms import CreateTaskForm
from task.models import Task


@login_required
def list_task(request):
  queryset = Task.objects.prefetch_related('category','assigned_to').all() # using eager load to avoid n+1 queries

  filter = TaskFilter(request.GET, queryset)
  order_by = request.GET.get('o', '-priority')
  queryset = filter.qs.order_by(order_by)

  context = {
    "sec_title": "Tasks",
    "tasks": queryset,
    "task_filter": filter
  }

  return render(request, 'list_task.html', context)


@login_required
def create_task(request):
  if request.method == 'POST':
    print(request.POST)
    form = CreateTaskForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('tasks')
  else:
    form = CreateTaskForm()

  context = {
    "form": form, 'sec_title': 'Create Task', 'btn_name': 'Create'
  }
  return render(request, 'create_task.html', context)
  

@login_required
def edit_task(request, pk):
  task = Task.objects.get(pk=pk)
  if request.method == 'POST':
    form = CreateTaskForm(request.POST, instance=task)
    if form.is_valid():
      form.save()
      return redirect('tasks')
  else:
    form = CreateTaskForm(instance=task)

  context = {
    "form": form, 'sec_title': 'Edit Task', 'btn_name': 'Update'
  }
  return render(request, 'create_task.html', context)


@login_required
def complete_task(request, pk):
  task = Task.objects.get(pk=pk)
  task.status = TASK_COMPLETED
  task.save()
  return redirect('tasks')


@login_required
def delete_task(request, pk):
  task = Task.objects.get(pk=pk)
  task.delete()
  return redirect('tasks')