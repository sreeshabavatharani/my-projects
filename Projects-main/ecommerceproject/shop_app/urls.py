from . import views
from django.urls import path

#name_space
app_name = 'shop'

urlpatterns =[
    path('', views.allprodCat, name="allprodCat"),
    path('<slug:c_slug>/', views.allprodCat, name="allprodCat"),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail, name='prodCatdetail'),
]