from django.http import HttpResponse, HttpResponseNotFound
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render

from .models import *



menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти',]


def index(request: WSGIRequest) -> HttpResponse:
    posts = Women.objects.all()
    content = {'posts': posts, 'menu': menu, 'title': 'Главная страница'}
    return render(request, 'women/index.html', content)


def about(request: WSGIRequest) -> render:
    content = {'menu': menu, 'title': 'О сайте'}
    return render(request, 'women/about.html', content)


def categories(request: WSGIRequest, cat_id: str) -> HttpResponse:
    return HttpResponse(f"Categories - {cat_id}")


def archive(request, year: int) -> HttpResponse or HttpResponseNotFound:
    if int(year) > 2022:
        return redirect('index')
    return HttpResponse(f"{year} archive")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найден!</h1>")
