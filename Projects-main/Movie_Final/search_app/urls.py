from django.urls import path
from . import views

app_name = 'searchapp'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('search_user/', views.search_user, name='search_user')
]