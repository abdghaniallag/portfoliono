from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post, Tag


def home(request):
    return render(request, 'base/index.html')


def posts(request):
    posts = Post.objects.filter(active=True)
    context = {"posts": posts}

    return render(request, 'base/posts.html',  context)


def post(request):
    return render(request, 'base/post.html')


def profile(request):
    return render(request, 'base/profile.html')
