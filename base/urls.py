 
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('index/', views.home,name='home'),
    path('posts/', views.posts,name='posts'),
    path('post/', views.post,name='post'), 
    path('profile/', views.profile,name='profile'),
]
