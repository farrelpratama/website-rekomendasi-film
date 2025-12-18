import requests
from django.conf import settings

def search_movies(query):
    try:
        response = requests.get(
            "http://omdbapi.com/",
            params={
                "apikey": settings.OMDB_API_KEY,
                "s": query
            },
            timeout=10
        )
        return response.json()
    except requests.exceptions.RequestException:
        return {"Response": "False"}

def get_movie_detail(imdb_id):
    try:
        response = requests.get(
            "http://omdbapi.com/",
            params={
                "apikey": settings.OMDB_API_KEY,
                "i": imdb_id,
                "plot": "full"
            },
            timeout=10
        )
        return response.json()
    except requests.exceptions.RequestException:
        return {"Response": "False"}
