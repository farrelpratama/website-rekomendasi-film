from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("<str:imdb_id>/", views.detail, name="detail"),
    path("bookmarks/add/", views.add_bookmark, name="add_bookmark"),
    path("bookmarks/remove/<str:imdb_id>/", views.remove_bookmark, name="remove_bookmark"),
]
