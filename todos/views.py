from django.urls import reverse_lazy
from django.views.generic import (
    ListView
)
from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalReadView,
    BSModalUpdateView,
    BSModalDeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Todo
from .forms import TodoForm

# Create your views here.
class TodoListView(ListView):
    model = Todo
    template_name = "home.html"
    context_object_name = "todos"
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(author=self.request.user)
            return queryset
        return queryset
    

class TodoCreateView(LoginRequiredMixin,BSModalCreateView):
    model = Todo
    template_name = "todo_new.html"
    form_class = TodoForm
    success_url = reverse_lazy("home")
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

class TodoDetailView(LoginRequiredMixin,BSModalReadView):
    model = Todo
    template_name = "todo_detail.html"

class TodoUpdateView(LoginRequiredMixin,BSModalUpdateView):
    model = Todo
    template_name = "todo_new.html"
    form_class = TodoForm
    success_url = reverse_lazy("home")

class TodoDeleteView(LoginRequiredMixin,BSModalDeleteView):
    model = Todo
    template_name = "todo_delete.html"
    success_url = reverse_lazy("home")
    success_message = "You have deleted action"
