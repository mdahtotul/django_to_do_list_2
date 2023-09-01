from django.shortcuts import render

from task.forms import CreateTaskForm

# Create your views here.
def get_all_tasks():
  pass 

def create_task(request):
  if request.method == 'POST':
    print(request.POST)
    form = CreateTaskForm(request.POST)

  else:
    form = CreateTaskForm()
    return render(request, 'create_task.html', {form: form})
  

def edit_task(request, pk):
  pass

def delete_task(request, pk):
  pass