from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView # using this one for the Registration Form
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm # also for Registration
from django.contrib.auth import login # for Registration so that after creating their account they dont have to login again
from .models import Task

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    # already authenticated user will be redirected away from this page
    redirect_authenticated_user = True

    def get_success_url(self):
        # sends them to the list of all the tasks
        return reverse_lazy('tasks')

 
class UserPage(FormView):
    template_name = "base/profile.html"
    form_class = UserCreationForm
    fields = "__all__"


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        # if user was sucessfully created use login
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)

# all the LoginRequiredMixin stuff in the classes is so that if ur not logged in you cant access that stuff so you cant look at specific stuff or edit it or delete it
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    # this is so that in the task_list.html file we can use the keyword tasks instead of object_list - for readability
    context_object_name = 'tasks'

    # I have not a clue but this stuff makes it so the users can only acess their own data
    # ** means keyword
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        # count of incomplete items
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith = search_input)

        context['search_input'] = search_input

        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

# neue task erstellen
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks') #after creating an item this line just sends the user back to the homepage list

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']# instead of listing all the fields like 'title, description, etc.' that make up a Task seperately we could also just use '__all__' but that would make it so a user could choose a different user to create a post for and we dont want that
    success_url = reverse_lazy('tasks')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')


# only users that are logged in can view user profiles
#@login_required
#class profile():
#    model = Task
#    context_object_name = 'task'
#    template_name = 'base/user/profile.html'

