from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path("",views.TodoList.as_view(), name="todo_list"),
    path('create/', views.TodoCreate.as_view(), name='todo_create'),
    path('<int:pk>/update/', views.TodoUpdate.as_view(), name='todo_update'),
    path('<int:pk>/remove/', views.TodoRemove.as_view(), name='todo_remove'),
]