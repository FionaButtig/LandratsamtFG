from django.contrib import admin
from .models import Task
from .models import Profile

# Register your models here.
# basically if you go to the Website and add /admin you get to the admin website where you can log in with your superuser and manage stuff and in that interface you have the 2 Sections "Groups" and "Users" and the next line adds anoterh one: "Task"
admin.site.register(Task)
admin.site.register(Profile)