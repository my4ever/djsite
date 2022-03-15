from django.http import HttpResponse, HttpResponseNotFound
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .forms import AddPostForm

from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]


def index(request: WSGIRequest) -> HttpResponse:
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context)


def about(request: WSGIRequest) -> render:
    context = {'menu': menu,
               'title': 'О сайте'}
    return render(request, 'women/about.html', context)


def contact(request):
    return HttpResponse("Contact")


def add_page(request):
    form = AddPostForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    form = AddPostForm()
    context = {
        'form': form,
        'menu': menu,
        'title': 'Добавить статью'
    }
    return render(request, 'women/addpage.html', context)


def login(request):
    return HttpResponse('login')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найден!</h1>")


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    context = {
        'post': post,
        'menu':  menu,
        'title': post.title,
        'cat_selected': post.cat.id
               }
    return render(request, 'women/post.html', context)


def show_category(request, cat_slug):
    posts = get_list_or_404(Women, cat__slug=cat_slug)
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': Category.objects.get(slug=cat_slug).id,
    }
    return render(request, 'women/index.html', context)
