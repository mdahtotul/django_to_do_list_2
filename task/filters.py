from unicodedata import category
from django import forms
from django_filters import FilterSet, DateFilter
import django_filters
from task.constants import TASK_PRIORITY, TASK_STATUS

from task.models import Category, Task

class CustomDateFilter(DateFilter):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.extra['widget'] = forms.DateInput(attrs={
      'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 inline-block w-full p-2.5 mb-2.5',
      'placeholder': 'Select a date',
      'type': 'date'
    })



class TaskFilter(FilterSet):
  start_date = CustomDateFilter(
    field_name='due_date',
    lookup_expr='gte', 
    label='From', 
  )
  end_date = CustomDateFilter(
    field_name='due_date',
    lookup_expr='lte', 
    label='To', 
  )

  status = django_filters.ChoiceFilter( 
    choices= TASK_STATUS,
    widget=forms.Select(attrs={
      'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 inline-block w-full p-2.5 mb-2.5',
    })
  )

  priority = django_filters.ChoiceFilter( 
    choices= TASK_PRIORITY,
    widget=forms.Select(attrs={
      'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 inline-block w-full p-2.5 mb-2.5',
    })
  )

  category = django_filters.ChoiceFilter( 
    choices= lambda: Category.objects.values_list('id','title'),
    widget=forms.Select(attrs={
      'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 inline-block w-full p-2.5 mb-2.5',
    })
  )

  class Meta:
    model = Task
    fields = ['category', 'status', 'priority', 'start_date', 'end_date']
    order_by = ['-priority', 'due_date']
    
    