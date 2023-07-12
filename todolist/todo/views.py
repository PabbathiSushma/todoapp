from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
#Home Page
def list_of_todos(request):
    todos = Todo.objects.all()
    context = {
        "todos" : todos
    }
    return render(request,"todos.html",context)


#Creating a new todo list
def todo_create(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form":form
    } 
    return render(request,"todo_create.html",context)


#Retriving one todo
def todo_retrive(request,pk):
    todos = Todo.objects.get(id=pk)
    context = {
        "todo" : todos
    }
    return render(request,"todo_retrive.html",context)


#update a todo
def todo_update(request,pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form":form
    } 
    return render(request,"todo_update.html",context)


#deleting a todo
def todo_delete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect("/")