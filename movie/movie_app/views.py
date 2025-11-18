from django.shortcuts import render, redirect
from django.views import View
from movie_app.forms import MovieForm
from movie_app.models import Movie


class Home(View):
    def get(self, request):
        movies = Movie.objects.all()   # fetch all movies
        return render(request, 'home.html', {'movies': movies})


class Add(View):
    def get(self, request):
        form_instance = MovieForm()
        return render(request, 'add_movie.html', {'form': form_instance})

    def post(self, request):
        form_instance = MovieForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('view')
        return render(request, 'add_movie.html', {'form': form_instance})

class View_movie(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'view.html', {'movies': movies})

from django.shortcuts import get_object_or_404

class Detail(View):
    def get(self, request, i):
        movie = get_object_or_404(Movie, id=i)
        return render(request, 'detail.html', {'movie': movie})


class Edit(View):
    def post(self,request,i):
        b = Movie.objects.get(id=i)
        form_instance = MovieForm(request.POST, request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('view')


    def get(self,request,i):
        b=Movie.objects.get(id=i)
        form_instance=MovieForm(instance=b)
        context={'form':form_instance}
        return render(request,'edit.html',context)

class Delete(View):
    def get(self, request, i):
            b = Movie.objects.get(id=i)
            b.delete()
            return redirect('view')

