from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo
# Create your views here.

def todoList(request): 
    context = {'todo_list':Todo.objects.all()}
    return render(request, 'todo/todo_list.html', context)

def insertItem(request:HttpRequest):
    todo = Todo(content = request.POST['content'])
    todo.save()
    return redirect('/todo/list')

def deleteItem(request, todo_id):
    delete_item = Todo.objects.get(id=todo_id)
    delete_item.delete()
    return redirect('/todo/list')
