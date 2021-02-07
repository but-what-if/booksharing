from django.shortcuts import render, get_object_or_404, redirect


from books.models import Book, Author, Log
from books.forms import BookForm, AuthorForm


def index(request):
    return render(request, 'index.html')


def books_create(request):
    form_data = request.POST
    if request.method == 'POST':
        form = BookForm(form_data)
        if form.is_valid():
            form.save()
            return redirect('books-list')
    elif request.method == 'GET':
        form = BookForm()

    context = {
        'message': "CREATE BOOK",
        'form': form
    }
    return render(request, 'books_create.html', context=context)


def books_list(request):
    context = {
        'books_list': Book.objects.all()
    }
    return render(request, 'books_list.html', context=context)


def books_update(request, pk):

    # try:
    #     book_obj = Book.objects.get(pk=pk)
    # except Book.DoesNotExist:
    #     raise Http404(f'Object with id: {pk} not found')
    instance = get_object_or_404(Book, pk=pk)

    form_data = request.POST
    if request.method == 'POST':
        form = BookForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('books-list')
    elif request.method == 'GET':
        form = BookForm(instance=instance)

    context = {
        'message': 'BOOK UPDATE',
        'form': form,
    }
    return render(request, 'books_create.html', context=context)


def books_delete(request, pk):
    instance = get_object_or_404(Book, pk=pk)
    instance.delete()
    return redirect('books-list')


def authors_create(request):
    data = request.POST
    if request.method == 'POST':
        form = AuthorForm(data)
        if form.is_valid():
            form.save()
            return redirect('authors-list')
    elif request.method == 'GET':
        form = AuthorForm()

    context = {
        'message': "CREATE AUTHOR",
        'form': form
    }
    return render(request, 'authors_create.html', context=context)


def authors_list(request):
    context = {
        'authors_list': Author.objects.all()
    }
    return render(request, 'authors_list.html', context=context)


def authors_update(request, pk):

    instance = get_object_or_404(Author, pk=pk)

    form_data = request.POST
    if request.method == 'POST':
        form = AuthorForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('authors-list')
    elif request.method == 'GET':
        form = AuthorForm(instance=instance)

    context = {
        'message': 'AUTHOR UPDATE',
        'form': form,
    }
    return render(request, 'authors_create.html', context=context)


def authors_delete(request, pk):
    instance = get_object_or_404(Author, pk=pk)
    instance.delete()
    return redirect('authors-list')


def logs_list(request):
    context = {
        'logs_list': Log.objects.all()
    }
    return render(request, 'logs.html', context=context)