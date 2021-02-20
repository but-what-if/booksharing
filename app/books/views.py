from books.models import Book, Author, Log
from books.forms import BookForm, AuthorForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView


class Index(TemplateView):
    template_name = 'index.html'


class BookCreate(CreateView):
    model = Book
    success_url = reverse_lazy('books-list')
    form_class = BookForm


class BookList(ListView):
    queryset = Book.objects.all()


class BookUpdate(UpdateView):
    model = Book
    success_url = reverse_lazy('books-list')
    form_class = BookForm


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books-list')


class AuthorCreate(CreateView):
    model = Author
    success_url = reverse_lazy('authors-list')
    form_class = AuthorForm


class AuthorList(ListView):
    queryset = Author.objects.all()


class AuthorUpdate(UpdateView):
    model = Author
    success_url = reverse_lazy('authors-list')
    form_class = AuthorForm


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors-list')


class LogList(ListView):
    queryset = Log.objects.all()
