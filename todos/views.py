from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context ={
        'todos': todos
    }
    return render(request, 'todos/index.html', context)


def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)


def new(request):
    return render(request, 'todos/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    priority = request.POST.get('priority')
    deadline = request.POST.get('deadline')

    todo = Todo(
                title=title,
                content=content,
                priority=priority,
                deadline=deadline
                )
    todo.save()

    return redirect('todos:index')


def edit(request, todo_pk):
    return render(request, 'todos/edit.html')


def update(request, todo_pk):
    return redirect('todos:detail', todo_pk)

def delete(request):
    return redirect('todos:index')