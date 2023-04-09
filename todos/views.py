from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    todos_num = Todo.objects.all().count()
    todos_done = Todo.objects.filter(completed=True).count()
    context ={
        'todos': todos,
        'todos_num': todos_num,
        'todos_done': todos_done,
    }
    return render(request, 'todos/index.html', context)


def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todos_num = Todo.objects.all().count()
    todos_done = Todo.objects.filter(completed=True).count()
    context ={
        'todo': todo,
        'todos_num': todos_num,
        'todos_done': todos_done,
    }
    return render(request, 'todos/detail.html', context)


def create(request):
    todos_num = Todo.objects.all().count()
    todos_done = Todo.objects.filter(completed=True).count()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm()
    context = {
        'form': form,
        'todos_num': todos_num,
        'todos_done': todos_done,
    }
    return render(request, 'todos/create.html', context)


def update(request, todo_pk):
    todos_num = Todo.objects.all().count()
    todos_done = Todo.objects.filter(completed=True).count()
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm(instance=todo)
    context = {
        'form': form,
        'todo': todo,
        'todos_num': todos_num,
        'todos_done': todos_done,
    }
    return render(request, 'todos/update.html', context)


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('todos:index')


def category(request):
    category_mode = request.GET.get('category_mode')
    if category_mode == '집안일':
        todos = Todo.objects.filter(category='집안일')
    elif category_mode == '문화생활':
        todos = Todo.objects.filter(category='문화생활')
    elif category_mode == '업무':
        todos = Todo.objects.filter(category='업무')
    elif category_mode == '자기계발':
        todos = Todo.objects.filter(category='자기계발')
    todos_num = Todo.objects.all().count()
    todos_done = Todo.objects.filter(completed=True).count()
    context = {
        'todos': todos,
        'todos_num': todos_num,
        'todos_done': todos_done,
    }
    return render(request, 'todos/index.html', context)