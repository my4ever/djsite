from django.urls import path
from .views import *


urlpatterns = [
    path('', WomenHome.as_view(), name='index'),
    path('about/', about, name='about'),
    path('addpage/', WomenAdd.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', WomenDetail.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
]
