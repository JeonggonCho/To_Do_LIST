from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm, CompleteForm

# Create your views here.
def index(request):
    todos_yet = Todo.objects.filter(completed=False)
    todos_done = Todo.objects.filter(completed=True)
    todos_num = Todo.objects.all().count()
    todos_done_num = Todo.objects.filter(completed=True).count()
    complete_form = CompleteForm()
    context = {
        'todos_yet': todos_yet,
        'todos_done': todos_done,
        'todos_num': todos_num,
        'todos_done_num': todos_done_num,
        'complete_form': complete_form,
    }
    return render(request, 'todos/index.html', context)


def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo,
    }
    return render(request, 'todos/detail.html', context)


def create(request):
    todos_num = Todo.objects.all().count()
    todos_done_num = Todo.objects.filter(completed=True).count()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form,
        'todos_num': todos_num,
        'todos_done_num': todos_done_num,
    }
    return render(request, 'todos/create.html', context)


def update(request, todo_pk):
    todos_num = Todo.objects.all().count()
    todos_done_num = Todo.objects.filter(completed=True).count()
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos:index')
    else:
        form = TodoForm(instance=todo)
    context = {
        'form': form,
        'todo': todo,
        'todos_num': todos_num,
        'todos_done_num': todos_done_num,
    }
    return render(request, 'todos/update.html', context)


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('todos:index')


def category(request):
    category_mode = request.GET.get('category_mode')
    if category_mode == '전체':
        todos_yet = Todo.objects.all()
    elif category_mode == '집안일':
        todos_yet = Todo.objects.filter(category='집안일')
    elif category_mode == '문화생활':
        todos_yet = Todo.objects.filter(category='문화생활')
    elif category_mode == '업무':
        todos_yet = Todo.objects.filter(category='업무')
    elif category_mode == '자기계발':
        todos_yet = Todo.objects.filter(category='자기계발')
    todos_num = Todo.objects.all().count()
    todos_done_num = Todo.objects.filter(completed=True).count()
    context = {
        'todos_yet': todos_yet,
        'todos_num': todos_num,
        'todos_done_num': todos_done_num,
    }
    return render(request, 'todos/index.html', context)


def sorting(request):
    print(request.GET.get('sorting_mode'))
    sorting_mode = request.GET.get('sorting_mode')
    if sorting_mode == '생성날짜순':
        todos_yet = Todo.objects.all().order_by('created_at')
    elif sorting_mode == '카테고리순':
        todos_yet = Todo.objects.all().order_by('category')
    elif sorting_mode == '마감날짜순':
        todos_yet = Todo.objects.all().order_by('deadline')
    context = {
        'todos_yet': todos_yet,
    }
    return render(request, 'todos/index.html', context)


# def completed(request):

#     return redirect('todos:index')