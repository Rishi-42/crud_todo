from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

from todo.models import Todo

class TodoList(ListView):
    model = Todo

class TodoCreate(CreateView):
    model = Todo
    fields = ['task']
    success_url= reverse_lazy('todo:todo_list')

class TodoUpdate(UpdateView):
    model = Todo
    fields = ['task']
    success_url= reverse_lazy('todo:todo_list')

class TodoRemove(DeleteView):
    model = Todo
    success_url= reverse_lazy('todo:todo_list')

