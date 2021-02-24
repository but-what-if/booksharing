from books.models import Book, Author, Log
from books.forms import BookForm, AuthorForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
# from pdb import set_trace; set_trace()


class FormUserKwargMixin:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class Index(TemplateView):
    template_name = 'index.html'


class BookCreate(FormUserKwargMixin, CreateView):
    model = Book
    success_url = reverse_lazy('books:my-books')
    form_class = BookForm


class BookList(ListView):
    queryset = Book.objects.all().select_related('author')


class MyBooksList(LoginRequiredMixin, ListView):
    queryset = Book.objects.all().select_related('author')
    template_name = 'books/my_books.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class BookUpdate(FormUserKwargMixin, UpdateView):
    model = Book
    success_url = reverse_lazy('books:my-books')
    form_class = BookForm


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books:list')


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
