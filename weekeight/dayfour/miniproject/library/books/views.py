from django.shortcuts import render
from .models import LibraryBooks, Author

libraryBooks = LibraryBooks.objects.all()

# Create your views here.
def virtualLibrary(request):
    return render(request, 'virtuallibrary.html', {'books': libraryBooks})

def myBook(request, booktitle):
    my_book = LibraryBooks.objects.get(title=booktitle)
    authors = my_book.author_set.all()
    return render(request, 'bookinfo.html', {'bookinfo': my_book, 'authors': authors})