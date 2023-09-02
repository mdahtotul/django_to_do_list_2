from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from task.forms import CreateTaskCategoryForm
from task.models import Category

@login_required
def list_category(request):
  queryset = Category.objects.all()
  return render(request, 'list_category.html', {"categories": queryset, 'sec_title': 'Category List'})


@login_required
def create_category(request):
  if request.method == 'POST':
    form = CreateTaskCategoryForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('create_category')
    else:
      print(form.errors)
  else:
    form = CreateTaskCategoryForm()

  context = {
    "form": form, 'sec_title': 'Create Category', 'btn_name': 'Create',
  }

  return render(request, 'create_category.html', context)


@login_required
def edit_category(request, pk):
  category = Category.objects.get(pk=pk)
  if request.method == 'POST':
    form = CreateTaskCategoryForm(request.POST, instance=category)
    if form.is_valid():
      form.save()
      return redirect('categories')
    else:
      print(form.errors)
  else:
    form = CreateTaskCategoryForm(instance=category)

  context = {
    "form": form, 'sec_title': 'Edit Category', 'btn_name': 'Update',
  }

  return render(request, 'create_category.html', context)


@login_required
def delete_category(request, pk):
  category = Category.objects.get(pk=pk)
  category.delete()
  return redirect('categories')