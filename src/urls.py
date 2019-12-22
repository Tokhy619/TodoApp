from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.todoList),
    path('insert/', views.insertItem, name="insertItem"),
    path('delete/<int:todo_id>', views.deleteItem, name="deleteItem"),

]