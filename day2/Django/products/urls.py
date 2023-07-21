from django.urls import path

# from .views import BookDetailView, BookListView
from .views import book_list, book_detail


urlpatterns = [
    #path("books", BookListView.as_view(), name="book-list"),
    # path("books/<int:pk>", BookListView.as_view(), name="book-detail")
    path("books", book_list, name="book-list"),
    path("books/<int:pk>", book_detail, name="book-detail")
]