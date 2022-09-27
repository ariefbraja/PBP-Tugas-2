from django.urls import path
from todolist.views import show_todolist
from todolist.views import register, login_user, logout_user, create_task, delete_task, change_status

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('delete-task/', delete_task, name='delete_task'),
    path('change-task-status/', change_status, name='change_status')
]