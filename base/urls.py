from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    # the ad_view() decides where to send the user after u click Logout - and we want to send em back to login
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name = 'register'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='tasks'),
    path('task-create', TaskCreate.as_view(), name='task-create'),
    # with task update and task detail, delete and update we need to target a specific task so thats why we write the <int:pk> at the end
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', DeleteView.as_view(), name='task-delete'),
]