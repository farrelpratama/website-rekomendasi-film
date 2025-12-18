from django.shortcuts import render
from django.http import HttpResponse
from .services import search_movies, get_movie_detail
from reviews.models import Review

def home(request):
    recommendations = search_movies("avengers")
    return render(request, "movies/home.html", {
        "recommendations": recommendations
    })

def search(request):
    movies = None
    query = request.GET.get("q")

    if query:
        movies = search_movies(query)
        print("OMDB response : ", movies)

    return render(request, "movies/search.html", {
        "movies": movies,
        "query": query
    })
# Create your views here.
def detail(request, imdb_id):
    movie = get_movie_detail(imdb_id)
    reviews = Review.objects.filter(imdb_id=imdb_id)

    if movie.get("Response") != "True":
        return render(request, "movies/detail.html", {
            "error": "Film tidak ditemukan"
        })

    return render(request, "movies/detail.html", {
        "movie": movie,
        "reviews": reviews
    })