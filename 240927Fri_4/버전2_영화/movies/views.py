from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)

# def new(request):
#     return render(request, 'movies/new.html')

def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid(): #유효성검사통과시
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form
    }
    return render(request, 'movies/create.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)

# def edit(request, movie_pk):
#     movie = Movie.objects.get(pk=movie_pk)
#     context = {
#         'movie': movie
#     }
#     return render(request, 'movies/edit.html', context)

def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid(): #유효성검사통과시
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie': movie,
        'form': form
    }
    return render(request, 'movies/update.html', context)

def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    return redirect('movies:index')