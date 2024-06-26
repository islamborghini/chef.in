# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipy/<int:pk>', views.recipy_detail, name='recipy_detail'),
    path('about', views.about, name='about'),
    path('category/<str:ggg>', views.category, name='category'),
    path('search', views.search, name='search'),
]
