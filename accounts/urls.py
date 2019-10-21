from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('accounts/register', views.RegisterFormView.as_view(), name="register"),
    path('accounts/login', views.LoginFormView.as_view(), name="login"),
    path('accounts/settings', views.UserSettingsView.as_view(), name="user_settings"),
    path('accounts/settings_edit', views.UserSettingsViewEdit.as_view(), name="settings_edit"),
    path('accounts/logged_out', views.LogoutFormView.as_view(), name="logout"),
]