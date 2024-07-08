from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import TodoItem
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def index(request):
    return HttpResponse('Hello There! its working')


# todoapp/views.py
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


# todoapp/views.py

@login_required
def home(request):
    todos = TodoItem.objects.filter(user=request.user)
    return render(request, 'home.html', {'todos': todos})

@login_required
def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        TodoItem.objects.create(user=request.user, title=title, description=description)
        return redirect('home')
    return render(request, 'add_todo.html')

@login_required
def delete_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    if todo.user == request.user:
        todo.delete()
    return redirect('home')
