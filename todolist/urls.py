from django.urls import path
from todolist.views import show_todolist, show_json, views_ajax, addTask_ajax, deleteTask_ajax
from todolist.views import register, login_user, logout_user, create_task, delete_task, change_status


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('delete-task/', delete_task, name='delete_task'),
    path('change-task-status/', change_status, name='change_status'),
    path('views-in-json/', show_json, name='show_json'),
    path('json/', views_ajax, name='views_ajax'),
    path('add/', addTask_ajax, name='addTask_ajax'),
    path('json/delete/<int:id>', deleteTask_ajax, name='deleteTask_ajax'),
]