from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Tag
from .forms import PostForm


def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]
    context = {"posts": posts}
    return render(request, 'base/index.html',  context)


def posts(request):
    posts = Post.objects.filter(active=True)
    context = {"posts": posts}

    return render(request, 'base/posts.html',  context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {"post": post}

    return render(request, 'base/post.html',  context)


def profile(request):
    return render(request, 'base/profile.html')


# CRUD VIEWS
@login_required(login_url='home')
def createPost(request):
    form = PostForm()
    context = {"form": form}
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')

    return render(request, 'base/post_form.html',  context)


@login_required(login_url='home')
def updatepost(request, pk):
    post= Post.objects.get(id=pk)
    form = PostForm(instance=post)
    context = {"form": form}
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')

    return render(request, 'base/post_form.html',  context)

@login_required(login_url='home')
def deletepost(request, pk):
    post= Post.objects.get(id=pk)
     
    context = {"post": post}
    if request.method == 'POST':
       post.delete()
       return redirect('posts')

    return render(request, 'base/delete.html',  context)
