# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView

# # models의 Author와 Book을 가져옴
# from .models import Author, Book

# # Create your views here.
# # 템플릿을 위한 view

# class BookListView(ListView):
#     model = Book
#     template_name = "book_list.html"


# class BookDetailView(DetailView):
#     model = Author
#     template_name = "book_detail.html"


from django.http import JsonResponse
from .models import Book, Author

def book_list(request):
    print('Request를 받았다')
    
    # book object를 모두 가져옴
    books = Book.objects.all()

    # books의 값을 list로 가져옴
    data = {"books": list(books.values())}

    # dictionary의 Json화
    response = JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii':False})

    return response

def book_detail(request, pk):
    book = Book.objects.get(pk=pk) # 특정 Book object를 가져옴

    data = {
        "book": {
            "author": book.author.name,
            "name": book.name,
            "description": book.description,
            "shipping_cost": book.shipping_cost,
            "quantity": book.quantity
        }
    }
    response = JsonResponse(data)
    return response