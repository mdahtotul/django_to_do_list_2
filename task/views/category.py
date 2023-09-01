from django.shortcuts import render, redirect

from task.forms import CreateTaskCategoryForm
from task.models import Category

def list_category(request):
  queryset = Category.objects.all()
  return render(request, 'list_category.html', {"categories": queryset, 'sec_title': 'Category List'})


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

  return render(request, 'create_category.html', {"form": form, 'sec_title': 'Create Category'})


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

  return render(request, 'create_category.html', {"form": form, 'sec_title': 'Edit Category'})


def delete_category(request, pk):
  category = Category.objects.get(pk=pk)
  category.delete()
  return redirect('categories')