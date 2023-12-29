from django import forms 
from bootstrap_modal_forms.forms import BSModalModelForm
from bootstrap_modal_forms.forms import BSModalForm

from .models import Todo


class TodoForm(BSModalModelForm):
    class Meta:
        model = Todo
        fields = ("title","action",)
        