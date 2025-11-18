from django.shortcuts import render, redirect
from django.views import View
from .forms import Add

from book.models import Book


books = []

class Add_book(View):
    def get(self, request):
        form_instance = Add()
        return render(request, 'addbooks.html', {'form': form_instance})

    def post(self, request):
        form_instance = Add(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            # title = form_instance.cleaned_data['title']
            # author = form_instance.cleaned_data['author']
            # price = form_instance.cleaned_data['price']
            # pages = form_instance.cleaned_data['pages']
            # language = form_instance.cleaned_data['language']
            # b=Book.objects.create(title=form_instance.cleaned_data['title'],author=form_instance.cleaned_data['author'],price=form_instance.cleaned_data['price'],pages=form_instance.cleaned_data['pages'],language=form_instance.cleaned_data['language'])
            # b.save()
            # books.append({
            #     'title': title,
            #     'author': author,
            #     'price': price,
            #     'pages': pages,
            #     'language': language,
            # })
            #
            #
            # return redirect('book:viewbooks')

        return render(request, 'addbooks.html', {'form': form_instance})


class ViewBooks(View):
    def get(self, request):
        b=Book.objects.all()
        context={"books":b}
        return render(request, 'viewbooks.html', {'books': b})

class Detail(View):
    def get(self,request,i):
        print(i)
        b=Book.objects.get(id=i)
        context={'book':b}

        return render(request,'detail.html',context)
class Del(View):
    def get(self, request, i):
        b = Book.objects.get(id=i)
        b.delete()
        return redirect('book:viewbooks')

class Edit_book(View):
    def post(self,request,i):
        b = Book.objects.get(id=i)
        form_instance = Add(request.POST, request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('book:viewbooks')


    def get(self,request,i):
        b=Book.objects.get(id=i)
        form_instance=Add(instance=b)
        context={'form':form_instance}
        return render(request,'edit.html',context)
# book/views.py
from django.views.generic import TemplateView

class Home(View):
    def get(self,request):
     return render(request, 'homepage.html')
