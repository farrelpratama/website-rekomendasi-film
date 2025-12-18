import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .services import search_movies, get_movie_detail
from django.contrib.auth.decorators import login_required
from reviews.models import Review
from .models import Bookmark
from .services import search_movies, get_movie_detail

def home(request):
    # =========================
    # RANDOM RECOMMENDATION
    # =========================
    random_data = search_movies("movie")
    random_movies = []

    if random_data and random_data.get("Response") == "True":
        random_movies = random_data.get("Search", [])
        random.shuffle(random_movies)
        random_movies = random_movies[:8]

    # =========================
    # BOOKMARK-BASED RECOMMENDATION
    # =========================
    bookmark_movies = []

    if request.user.is_authenticated:
        bookmarks = Bookmark.objects.filter(user=request.user)

        keywords = set()
        for b in bookmarks:
            # Ambil kata pertama judul (simple & aman)
            keywords.add(b.title.split()[0])

        for keyword in keywords:
            data = search_movies(keyword)
            if data and data.get("Response") == "True":
                bookmark_movies.extend(data.get("Search", []))

        random.shuffle(bookmark_movies)
        bookmark_movies = bookmark_movies[:8]

    return render(request, "movies/home.html", {
        "random_movies": random_movies,
        "bookmark_movies": bookmark_movies
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