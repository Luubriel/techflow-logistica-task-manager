from django.contrib.auth.views import LoginView, logout_then_login

class UserLoginView(LoginView):
    template_name="authentication/login.html"

def user_logout(request):
    return logout_then_login(request)