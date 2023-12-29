from django.urls import reverse_lazy
from django.conf import settings
from bootstrap_modal_forms.generic import BSModalCreateView
from bootstrap_modal_forms.generic import BSModalLoginView
from django.contrib.auth.views import LogoutView

from .forms import CustomUserCreationForm, CustomAuthenticationForm


# Create your views here.


class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"
    success_message = 'Success: Account was created.'

class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "registration/login.html"
    success_url = reverse_lazy("home")
    extra_context = dict(success_url=reverse_lazy('base'))

class CustomLogoutView(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL