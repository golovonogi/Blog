from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        user=form.save()
        auth_login(self.request, user)
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(LoginView):
    success_url = '/'
    template_name = 'accounts/login.html'

