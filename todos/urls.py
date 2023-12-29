from django.urls import path

from .views import (
    TodoListView,
    TodoCreateView,
    TodoDetailView,
    TodoUpdateView,
    TodoDeleteView
)

urlpatterns = [
    path("", TodoListView.as_view(), name="home" ),
    path("new/", TodoCreateView.as_view(), name="new_todo" ),
    path("read/<int:pk>", TodoDetailView.as_view(), name="todo_detail"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
]