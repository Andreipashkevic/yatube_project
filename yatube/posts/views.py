#from turtle import title
from re import template
from turtle import title
from django.shortcuts import get_object_or_404, render
from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    #title = 'Главная страница'
    #text = 'Последние обновления'
    context = {
        'posts': posts,
        #'title': title,
        #'text': text,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)