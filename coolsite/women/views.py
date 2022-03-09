from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect


def index(request: WSGIRequest) -> HttpResponse:
    return HttpResponse("index")


def categories(request: WSGIRequest, cat_id: str) -> HttpResponse:
    user = {'first name': request.GET['first'],
                   'last name': request.GET['last']}
    return HttpResponse(f"Categories - {cat_id}")


def archive(request, year: int) -> HttpResponse or HttpResponseNotFound:
    if int(year) > 2022:
        return redirect('index')
    return HttpResponse(f"{year} archive")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найден!</h1>")
