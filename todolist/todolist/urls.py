from django.contrib import admin
from django.urls import path
from todo.views import ( 
    list_of_todos,
    todo_create,
    todo_retrive,
    todo_update,
    todo_delete
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",list_of_todos),
    path("add-todo/",todo_create),
    path("<pk>/",todo_retrive),
    path("<pk>/edit/",todo_update),
    path("<pk>/delete/",todo_delete)
]
