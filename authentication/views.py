from django.contrib.auth.views import LoginView, logout_then_login
from .forms import CustomLoginForm

class UserLoginView(LoginView):
    template_name="authentication/login.html"
    authentication_form=CustomLoginForm

def user_logout(request):
    return logout_then_login(request)