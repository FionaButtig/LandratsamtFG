from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class TaskList(ListView):
    model = Task
    # this is so that in the task_list.html file we can use the keyword tasks instead of object_list - for readability
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

# neue task erstellen
class TaskCreate(CreateView):
    model = Task
    fields = '__all__' # instead of listing all the fields like 'title, description, etc.' that make up a Task seperately
    success_url = reverse_lazy('tasks') #after creating an item this line just sends the user back to the homepage list

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
