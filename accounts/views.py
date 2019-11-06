from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth import login as auth_login

from accounts.forms import UserSettings


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(LoginView):
    template_name = 'accounts/login.html'

    def get_redirect_url(self):
        return '/'


class LogoutFormView(LogoutView):
    next_page = '/'

class UserSettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/settings.html'

class UserSettingsViewEdit(LoginRequiredMixin, UpdateView):
    form_class = UserSettings
    success_url = reverse_lazy('accounts:user_settings')
    template_name = 'accounts/settings_edit.html'

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return super(UserSettingsViewEdit, self).form_valid(form)


