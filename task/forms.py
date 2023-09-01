from django import forms

from task.models import Category, Task


class CreateTaskCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2.5"
                }
            ),
        }


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "details"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2.5"
                }
            ),
            "details": forms.TextInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:border-2 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2.5"
                }
            ),
        }
