from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('accounts/register', views.RegisterFormView.as_view(), name="register"),
    path('accounts/login', views.LoginFormView.as_view(), name="login"),
]