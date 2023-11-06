from django.db import models
# a Model Procived by Django that takes care of User information like email, passwort, etc.
from django.contrib.auth.models import User

# Create your models here.


# The class for a Task - Like if you want to add the Task "Do Homework" it has a user, a title "Do Homework", a description, a status (if its been completed or not) and a time when it was created
class Task(models.Model):
    # need to create a many-to-one relationship - one user can have many items
    # on_delete=models.CASCADE means that if the user is deleted then all the Tasks connected to the User will be deleted too
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # null=True means that the field could be left empty
    # blank=True means that the field starts out as blank
    # But every Task needs a title so we dont want that field to stay blank so we dont add those 2 to the title thing
    title = models.CharField(max_length=200)
    # CharField is usually used for shorter simpler stuff and Textfiled for more text
    description = models.TextField(null=True, blank=True) 
    # when the items is first created its probably not completed yet so we want it to be False by default
    complete = models.BooleanField(default=False)
    # auto_now_add basically takes a screenshot of when it was created and just uses that as the creation time
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        # completed Tasks at the bottom of the List
        ordering = ["complete"]




# after making this new model we have to do a migration - to migrate this new model to the database that Django provided
# the command for this is:      python manage.py makemigrations
# this creates a new file in the migrations folder
# and after that run the command: python manage.py migrate
