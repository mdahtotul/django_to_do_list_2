from django.shortcuts import render, redirect

from task.forms import CreateTaskCategoryForm, CreateTaskForm
from task.models import Category



def get_all_tasks():
  pass 

def create_task(request):
  if request.method == 'POST':
    print(request.POST)
    form = CreateTaskForm(request.POST)

  else:
    form = CreateTaskForm()
    return render(request, 'create_task.html', {"form": form, 'sec_title': 'Create Task'})
  

def edit_task(request, pk):
  pass

def delete_task(request, pk):
  pass