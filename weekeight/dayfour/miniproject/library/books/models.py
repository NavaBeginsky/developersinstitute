from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class LibraryBooks(models.Model):
    title = models.CharField(max_length=250)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def checkAvailable(self):
        if self.id in CurrentlyCheckedOutBy.objects.values_list('book', flat=True):
            return False
        return True

class Author(models.Model):
    name = models.CharField(max_length=100, default=None)
    books = models.ManyToManyField(LibraryBooks)

    def __str__(self):
        return self.name

class CurrentlyCheckedOutBy(models.Model):
    book = models.OneToOneField(LibraryBooks, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name + ' ' + self.book.title
    