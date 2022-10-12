from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.forms import TodolistForm
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.utils import timezone

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
        'data_todolist': data_todolist,
    }
    return render(request, "todolist.html", context)

def delete_task(request):
    if request.method == "POST":
        todo = Task.objects.get(id=request.POST["id"])
        todo.delete()
    return redirect('todolist:show_todolist')

def change_status(request):
    if request.method == "POST":
        todo = Task.objects.get(id=request.POST["id"])
        todo.is_finished = not todo.is_finished
        todo.save()
    return redirect('todolist:show_todolist')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def create_task(request):
    form = TodolistForm()

    if request.method == "POST":
        form = TodolistForm(request.POST)
        if form.is_valid():
            saving = form.save(commit=False)
            saving.user=User.objects.get(username=request.user.username)
            saving.save()
            return redirect('todolist:show_todolist')

    context = {'form':form}
    return render(request, 'create-task.html', context)

def show_json(request):
    data_todolist = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data_todolist))

def add_task_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")

        new_todolist = Task(title=title, description=description, user=request.user)
        new_todolist.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def delete_task_ajax(request, id):
    data = Task.objects.filter(user=request.user).get(pk=id)
    data.delete()

    return HttpResponse(b"DELETED", status=201)

def views_ajax(request):
    return render(request, "todolist-ajax.html")