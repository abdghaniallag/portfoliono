 
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('index/', views.home,name='home'),
    path('posts/', views.posts,name='posts'),
    path('post/<str:pk>', views.post,name='post'), 
    path('profile/', views.profile,name='profile'),
    # CRUD URLS 
    path('createpost/', views.createPost,name='createpost'),
    path('updatepost/<str:pk>', views.updatepost,name='updatepost'),
    path('deletepost/<str:pk>', views.deletepost,name='deletepost'),
    path('sendemail/', views.sendEmail,name='sendemail'),
]
