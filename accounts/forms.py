from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser

class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin,
                             UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', "email",
                  "age", 'password1', 'password2', ]
        

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
