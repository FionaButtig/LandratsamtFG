from django.urls import path
from . import views
from .views import TaskList
from .views import TaskDetail

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='tasks'),
]