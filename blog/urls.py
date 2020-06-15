from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('author/', views.author, name='author'),
    path('category/<category>/', views.blog_category, name='blog_category'),
    path('<str:slug>/', views.blog_detail, name='blog_detail'),
]