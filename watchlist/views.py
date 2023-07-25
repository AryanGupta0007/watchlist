from django.shortcuts import render
from .models import Movies
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    if request.method == 'POST':
        print('hi')
        try:
            movie_name = request.POST['movieName'].title()
            platform_name = request.POST['platformName'].title()
            entry = Movies(movie_name=movie_name, platform_name=platform_name)
            entry.save()
            # print(f"{movie_name} streaming on {platform_name}")

        except:
            movie_id = request.POST['movie_id']
            # print(movie_id)
            movie = Movies.objects.get(pk=movie_id)
            if movie:
                movie.delete()
            else:
                pass

        finally:
            return HttpResponseRedirect(reverse('index'))

    elif request.method == 'GET':
        movies = Movies.objects.all()
        # print(movies)
        return render(request, 'watchlist/index.html', {
            'movies': movies
        })
