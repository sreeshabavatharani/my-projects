from django.urls import path
from . import views

app_name = 'movieapp'

urlpatterns=[
    path('',views.home,name='home'),
    path('add/', views.add_movie, name='add_movie'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('home_second/', views.home_second, name='home_second'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('review_movie/<int:id>', views.review_movie, name='review_movie'),
    path('display_review/<int:id>/', views.display_review, name='display_review'),
    path('movie_categroy/<int:id>/', views.movie_categroy, name='movie_categroy'),
]