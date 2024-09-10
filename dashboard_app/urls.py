from django.urls import path
from .views import artist_profile_view, artists_view, artist_detail_view, track_detail_view, add_to_playlist, trending_music, video_list, dashboard_view
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('artist/<str:artist_id>/', artist_profile_view, name='artist_profile'),
    path('artists/', artists_view, name='artists'),
    path('artist/<str:artist_id>/', artist_detail_view, name='artist_detail'),  # Potential conflict here
    path('track/<str:track_id>/', track_detail_view, name='track_detail'),
    path('add_to_playlist/<str:track_id>/', add_to_playlist, name='add_to_playlist'),
    path('trending/', trending_music, name='trending_music'),
    path('videos/', video_list, name='video_list'),
]
