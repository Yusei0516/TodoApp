from django.urls import path
from .views import TodoList, TodoCreate, TodoUpdate, TodoDelete

app_name = "todos"

urlpatterns = [
    path("", TodoList.as_view(), name="list"),
    path("new/", TodoCreate.as_view(), name="create"),
    path("<int:pk>/edit/", TodoUpdate.as_view(), name="update"),
    path("<int:pk>/delete/", TodoDelete.as_view(), name="delete"),
]
