from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Tag
from .forms import PostForm
from .filters import PostFilte
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]
    context = {"posts": posts}
    return render(request, 'base/index.html',  context)


def posts(request):
    posts = Post.objects.filter(active=True)
    postfilter = PostFilte(request.GET, queryset=posts)
    posts = postfilter.qs
    page = request.GET.get('page')
    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {"posts": posts, "postfilter": postfilter}

    return render(request, 'base/posts.html',  context)


def post(request, slug):
    post = Post.objects.get(slug=slug)
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
def updatepost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    context = {"form": form}
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')

    return render(request, 'base/post_form.html',  context)


@login_required(login_url='home')
def deletepost(request, slug):
    post = Post.objects.get(slug=slug)

    context = {"post": post}
    if request.method == 'POST':
        post.delete()
        return redirect('posts')

    return render(request, 'base/delete.html',  context)


def sendEmail(request):
    if request.method == 'POST':
        template = render_to_string('base/email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })
        email = EmailMessage(request.POST['subject'],
                             template,
                             settings.EMAIL_HOST_USER,
                             ['abdghaniallag@gmail.com'],)
        email.fail_silently = False
        email.send() 
    return render(request, 'base/email_template.html')
