from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Todo
from .forms import TodoForm

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("todos:list")
    else:
        form = UserCreationForm()
    return render(request, "auth/signup.html", {"form": form})

class OwnerOnlyMixin(UserPassesTestMixin):
    """
    URLパラメータのpkで対象Todoを取得し、
    それが自分のものか（所有者チェック）を行う。
    """
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

class TodoList(LoginRequiredMixin, ListView):
    """
    自分のToDoだけを表示する一覧
    """
    model = Todo
    template_name = "todos/list.html"
    context_object_name = "todos"

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

class TodoCreate(LoginRequiredMixin, CreateView):
    """
    新規作成。ModelFormを使い、保存前に所有者を自分へセット。
    """
    model = Todo
    form_class = TodoForm
    template_name = "todos/form.html"
    success_url = reverse_lazy("todos:list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)

class TodoUpdate(LoginRequiredMixin, OwnerOnlyMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "todos/form.html"
    success_url = reverse_lazy("todos:list")

class TodoDelete(LoginRequiredMixin, OwnerOnlyMixin, DeleteView):
    model = Todo
    template_name = "todos/confirm_delete.html"
    success_url = reverse_lazy("todos:list")
# Create your views here.

