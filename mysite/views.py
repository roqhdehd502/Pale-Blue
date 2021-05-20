from django.views.generic import TemplateView, CreateView

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.mixins import AccessMixin

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

class OwnerOnlyMixin(AccessMixin): # 로그인한 사용자가 콘텐츠의 소유자인지 판별하는 클래스
    raise_exception = True # 소유자가 아닌경우 True 처리하여 403 예외 처리를 하거나 소유자 일경우 false 처리하여 로그인 페이지로 리다이렉트 처리 한다
    permission_denied_message = "Owner Only can update/delete the object"

    def dispatch(self, request, *args, **kwargs): # 해당 메소드를 통해 소유자인지 판별한다
        obj = self.get_object()
        
        if request.user != obj.owner: # 현재 사용자랑 해당(객체) 사용자가 다르면 handle_no_permission() 메소드를 호출하여 403 예외 처리를 한다
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)