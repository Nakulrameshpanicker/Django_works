from django.contrib import admin
from django.template.context_processors import request
from book.models import Book


# Register your models here.
admin.site.register(Book)