from django.shortcuts import render, redirect
from django.http import HttpResponse
from .services import search_movies, get_movie_detail
from django.contrib.auth.decorators import login_required
from reviews.models import Review
from .models import Bookmark

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

    is_bookmarked = False
    if request.user.is_authenticated:
        is_bookmarked = Bookmark.objects.filter(
            user=request.user,
            imdb_id=imdb_id
        ).exists()

    return render(request, "movies/detail.html", {
        "movie": movie,
        "reviews": reviews,
        "is_bookmarked": is_bookmarked
    })

@login_required
def add_bookmark(request):
    if request.method == "POST":
        imdb_id = request.POST.get("imdb_id")

        Bookmark.objects.get_or_create(
            user=request.user,
            imdb_id=imdb_id,
            title=request.POST.get("title"),
            poster=request.POST.get("poster"),
        )

        return redirect("detail", imdb_id=imdb_id)

@login_required
def remove_bookmark(request, imdb_id):
    Bookmark.objects.filter(
        user=request.user,
        imdb_id=imdb_id
    ).delete()

    return redirect("detail", imdb_id=imdb_id)