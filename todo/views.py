from django.shortcuts import render, redirect

from todo.forms import TodoForm
from .models import Todo

# Create your views here.
def list(request):
    todos = Todo.objects.all()
    context = {
        'todos':todos
    }
    return render(request,'todo/home.html', context)

def update(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        return redirect('todo-home')
    context = {'form':form}
    return render(request, 'todo/todo_form.html', context)

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo-home')
    return render(request, 'todo/delete.html', {'todo':todo})