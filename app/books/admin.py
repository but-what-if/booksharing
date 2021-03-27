from django.contrib import admin
from books.models import Book, RequestBook, Author


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'publish_year',
        'review',
        'condition',
        'category',
        'user',
        'author',
    )
    readonly_fields = (
        'title',
        'publish_year',
        'review',
        'category',
        'author',
    )
    list_filter = ('category', 'condition',)
    search_fields = ('title', 'author')


admin.site.register(Book, BookAdmin)


class RequestBookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'recipient',
        'book',
        'created',
        'status',
    )
    readonly_fields = ('recipient', 'book')
    list_filter = ('status', 'created', )
    search_fields = ('recipient__username', 'recipient__last_name')
    # list_select_related = ('recipient', 'book')  # objects.select_related('recipient', 'book')

    # def get_readonly_fields(self, request, obj=None):
    #     readonly_fields = super().get_readonly_fields()

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(RequestBook, RequestBookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'date_of_birth',
        'date_of_death',
        'country',
        'gender',
        'language',
    )
    readonly_fields = (
        'first_name',
        'last_name',
        'date_of_birth',
        'country',
        'gender',
    )
    list_filter = ('country', 'language', )
    search_fields = ('first_name', 'last_name')


admin.site.register(Author, AuthorAdmin)
