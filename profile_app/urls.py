from django.urls import path
from . import views


urlpatterns = [
    path("", views.profile, name="profile"),
    path("downloads/", views.downloads, name="downloads"),
    path("albums/", views.albums, name="albums"),
    path("playlists/", views.playlists, name="playlists"),
    path("favorites/", views.favorites, name="favorites"),
]