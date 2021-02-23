from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index),
    path('', views.TaskList.as_view(), name='task-list'),
    path('newtask/', views.TaskForm.as_view(), name='new-task'),
    path('archivedtask/', views.ArchivedTaskList.as_view(),name='archived-task'),
    path('updatetask/<int:pk>/', views.EditTask.as_view(), name='update-task'),
    path('detailtask/<int:pk>/', views.DetailTask.as_view(), name='detail-task'),
    path('archivedtasks/', views.ArchivedTask.as_view(), name='archived-task'),

]
