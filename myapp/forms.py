# myapp/forms.py

from django import forms
from .models import Author, Book, Publisher


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'age']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'})
        }
        


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['Nombre', 'Direccion', 'Ciudad', 'Estado_o_Provincia', 'Pais', 'Website']


class SearchForm(forms.Form):
    search_text = forms.CharField(max_length=100)
