from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    path('create/', views.BookCreate.as_view(), name='create'),
    path('list/', views.BookList.as_view(), name='list'),
    path('list/my-books/', views.MyBooksList.as_view(), name='my-books'),
    path('list/my-authors/', views.MyAuthorsList.as_view(), name='my-authors'),
    path('authors/create/', views.AuthorCreate.as_view(), name='authors-create'),
    path('authors/list/', views.AuthorList.as_view(), name='authors-list'),
    path('update/<int:pk>/', views.BookUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.BookDelete.as_view(), name='delete'),
    path('download-csv/', views.DownloadCSVBookView.as_view(), name='download-csv'),
    path('download-xlsx/', views.DownloadXLSXBookView.as_view(), name='download-xlsx'),
    path('authors/download-csv/', views.DownloadCSVAuthorView.as_view(), name='authors-download-csv'),
    path('authors/download-xlsx/', views.DownloadXLSXAuthorView.as_view(), name='authors-download-xlsx'),
    path('authors/update/<int:pk>/', views.AuthorUpdate.as_view(), name='authors-update'),
    path('authors/delete/<int:pk>/', views.AuthorDelete.as_view(), name='authors-delete'),
]
