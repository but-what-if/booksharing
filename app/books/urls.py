from django.urls import path
from books import views

urlpatterns = [
    path('create/', views.BookCreate.as_view(), name='books-create'),
    path('list/', views.BookList.as_view(), name='books-list'),
    path('authors/create/', views.AuthorCreate.as_view(), name='authors-create'),
    path('authors/list/', views.AuthorList.as_view(), name='authors-list'),
    path('update/<int:pk>/', views.BookUpdate.as_view(), name='books-update'),
    path('delete/<int:pk>/', views.BookDelete.as_view(), name='books-delete'),
    path('authors/update/<int:pk>/', views.AuthorUpdate.as_view(), name='authors-update'),
    path('authors/delete/<int:pk>/', views.AuthorDelete.as_view(), name='authors-delete'),
]