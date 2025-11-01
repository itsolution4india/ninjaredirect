from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('fodie/', views.foodie, name='fodie'),
    path('logvisitor/<int:id>', views.gotbaited, name='bait_user'),
]
