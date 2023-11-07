from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

# Create your views here.

class TaskList(ListView):
    model = Task
    # this is so that in the task_list.html file we can use the keyword tasks instead of object_list - for readability
    context_object_name = "tasks"

class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "base/task.html"

