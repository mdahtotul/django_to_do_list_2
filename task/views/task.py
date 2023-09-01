from django.shortcuts import render, redirect

from task.forms import CreateTaskForm
from task.models import Task



def list_task(request):
  queryset = Task.objects.prefetch_related('category','assigned_to').all() # using eager load to avoid n+1 queries
  context = {
    "sec_title": "Tasks",
    "tasks": queryset,
  }

  return render(request, 'list_task.html', context)


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
  

def edit_task(request, pk):
  task = Task.objects.get(pk=pk)
  if request.method == 'POST':
    print(request.POST)
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


def delete_task(request, pk):
  task = Task.objects.get(pk=pk)
  task.delete()
  return redirect('tasks')