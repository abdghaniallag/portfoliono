 
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('index/', views.home,name='home'),
    path('posts/', views.posts,name='posts'),
    path('post/<slug:slug>', views.post,name='post'), 
    path('profile/', views.profile,name='profile'),
    # CRUD URLS 
    path('createpost/', views.createPost,name='createpost'),
    path('updatepost/<slug:slug>', views.updatepost,name='updatepost'),
    path('deletepost/<slug:slug>', views.deletepost,name='deletepost'),
    path('sendemail/', views.sendEmail,name='sendemail'),
]
