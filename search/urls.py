from django.urls import path
from . import views


app_name = 'search'

urlpatterns = [
    path('search/search_index', views.SearchView.as_view(), name='search')
]