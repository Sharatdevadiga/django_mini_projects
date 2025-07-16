from django.shortcuts import render
from book_outlet.models import Book
import django.http
from django.http import HttpResponseNotFound

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {
        "books": books
    })

def book_details(request, slug):
    try:
        book = Book.objects.get(slug=slug)
    except:
        return HttpResponseNotFound("Book not found")
    return render(request, "book_outlet/book_details.html", {
        "book": book
    })