# from django.urls import path
from rest_framework.routers import DefaultRouter
from books.api import views

app_name = 'books-api'

# urlpatterns = [
#     path('api/v1/books/', BookList.as_view()),
#     path('api/v1/books/<int:pk>/', BookInstanceView.as_view())
# ]


router = DefaultRouter()
router.register(r'books', views.BookModelViewSet, basename='book')
router.register(r'authors', views.AuthorModelViewSet, basename='author')
router.register(r'categories', views.CategoryModelViewSet, basename='category')
urlpatterns = router.urls
