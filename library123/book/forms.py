from django import forms
from book.models import Book




# class Add(forms.Form):
#     title=forms.CharField()
#     author=forms.CharField()
#     price=forms.IntegerField()
#     pages=forms.IntegerField()
#     language=forms.CharField()

class Add(forms.ModelForm): #all the forms are automatically called
    class Meta: #inner class used to define the structure of form.
        model=Book
        fields="__all__"