"""booksharing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index'),
    path('books/create/', views.books_create, name='books-create'),
    path('books/list/', views.books_list, name='books-list'),
    path('books/authors/create/', views.authors_create, name='authors-create'),
    path('books/authors/list/', views.authors_list, name='authors-list'),
    path('books/update/<int:pk>/', views.books_update, name='books-update'),
    path('books/delete/<int:pk>/', views.books_delete, name='books-delete'),
    path('books/authors/update/<int:pk>/', views.authors_update, name='authors-update'),
    path('books/authors/delete/<int:pk>/', views.authors_delete, name='authors-delete'),
]
