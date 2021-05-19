from django.views.generic import TemplateView, CreateView

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# HomepageView
class HomeView(TemplateView):
    template_name = 'home.html'

# User Creation
class UserCreateView(CreateView): # /accounts/register URL을 처리하는 클래스
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView): # /accounts/register/done URL을 처리하는 클래스
    template_name = 'registration/register_done.html'