from django import forms
from .models import Book

class AuthorForm(forms.Form):
    name = forms.CharField(label="Author Name", max_length=100)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']