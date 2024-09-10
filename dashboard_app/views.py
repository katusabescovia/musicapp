from django.shortcuts import render,redirect
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .models import Search
from .filters import SearchFilter
from django.shortcuts import render
from .youtube_client import search_videos
from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.shortcuts import render
from googleapiclient.discovery import build
from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.shortcuts import render
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

def artist_profile_view(request, artist_id):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id='0690e4be447b478caaa0acd30050e91d',
        client_secret='1b1436c8af7843f980f3d8513c1830b3'
    ))

    artist = sp.artist(artist_id)
    tracks = sp.artist_top_tracks(artist_id)['tracks']

    context = {
        'artist': artist,
        'tracks': tracks
    }
    return render(request, 'dashboard/artist_profile.html', context)



def dashboard_view(request):
    sp = Spotify(auth_manager=SpotifyClientCredentials(
        client_id='0690e4be447b478caaa0acd30050e91d',
        client_secret='1b1436c8af7843f980f3d8513c1830b3'
    ))

    artist_name = request.GET.get('artist_name')
    category = request.GET.get('category')
    country = request.GET.get('country')

    query = ""
    if artist_name:
        query += f'artist:{artist_name} '
    if category:
        query += f'genre:{category} '
    if country:
        query += f'country:{country}'

    results = []
    if query:
        search_results = sp.search(q=query.strip(), type='track')
        for track in search_results['tracks']['items']:
            results.append({
                'id': track['id'],  # Ensure track ID is included
                'name': track['name'],
                'artist_name': track['artists'][0]['name'],
                'artist_id': track['artists'][0]['id'],
                'album_name': track['album']['name'],
                'album_image_url': track['album']['images'][0]['url'],
                'preview_url': track['preview_url']
            })
    else:
        default_query = 'pop'
        search_results = sp.search(q=default_query, type='track', limit=5)
        for track in search_results['tracks']['items']:
            results.append({
                'id': track['id'],  # Ensure track ID is included
                'name': track['name'],
                'artist_name': track['artists'][0]['name'],
                'artist_id': track['artists'][0]['id'],
                'album_name': track['album']['name'],
                'album_image_url': track['album']['images'][0]['url'],
                'preview_url': track['preview_url']
            })

    search_filter = SearchFilter(request.GET, queryset=Search.objects.none())

    return render(request, 'dashboard/dashboard.html', {'filter': search_filter, 'results': results})



def fetch_artists(sp, query, limit=20):
    search_results = sp.search(q=query, type='artist', limit=limit)
    artists = []
    for artist in search_results['artists']['items']:
        artists.append({
            'name': artist['name'],
            'id': artist['id'],
            'image_url': artist['images'][0]['url'] if artist['images'] else None
        })
    return artists



def fetch_artists(sp, query, limit=20):
    search_results = sp.search(q=query, type='artist', limit=limit)
    artists = []
    for artist in search_results['artists']['items']:
        artists.append({
            'name': artist['name'],
            'id': artist['id'],
            'image_url': artist['images'][0]['url'] if artist['images'] else None
        })
    return artists

def artists_view(request):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id='0690e4be447b478caaa0acd30050e91d',
        client_secret='1b1436c8af7843f980f3d8513c1830b3'
    ))

    # Define queries for different artist categories
    queries = {
        'European Artists': 'genre:pop',
        'African Artists': 'genre:african',
        'Ugandan Artists': 'Ugandan',  # Adjusted to include specific names or terms
        'Nigerian Artists': 'Nigerian',
        'Kenyan Artists': 'Kenyan'
    }

    # Fetch artists for each category
    artists_data = {}
    for category, query in queries.items():
        artists_data[category] = fetch_artists(sp, query)

    return render(request, 'dashboard/artists.html', {'artists_data': artists_data})

def artist_detail_view(request, artist_id):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id='0690e4be447b478caaa0acd30050e91d',
        client_secret='1b1436c8af7843f980f3d8513c1830b3'
    ))

    artist = sp.artist(artist_id)
    albums = sp.artist_albums(artist_id, album_type='album')['items']

    return render(request, 'dashboard/artist_detail.html', {
        'artist': artist,
        'albums': albums
    })



def track_detail_view(request, track_id):
    # Initialize Spotipy with Spotify credentials
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id='0690e4be447b478caaa0acd30050e91d',
        client_secret='1b1436c8af7843f980f3d8513c1830b3'
    ))

    try:
        # Fetch track details from Spotify
        track = sp.track(track_id)
    except spotipy.exceptions.SpotifyException:
        raise Http404("Track not found")

    # Pass the track details to the template
    context = {
        'track': track
    }
    return render(request, 'dashboard/track_detail.html', context)
def add_to_playlist(request, track_id):
    if request.method == 'POST':
        user_spotify = spotipy.Spotify(auth=request.user.social_auth.get(provider='spotify').access_token)
        try:
            user_spotify.user_playlist_add_tracks(user=request.user.username, playlist_id='your_playlist_id', tracks=[track_id])
            message = "Track added to your playlist successfully!"
        except spotipy.exceptions.SpotifyException as e:
            message = "Failed to add track to playlist."

        return render(request, 'dashboard/add_to_playlist_result.html', {'message': message})
    else:
        return redirect('artist_profile', artist_id=request.GET.get('artist_id'))
    
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

def get_spotify_client():
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="0690e4be447b478caaa0acd30050e91d",
                                                                client_secret="1b1436c8af7843f980f3d8513c1830b3"))



def get_trending_tracks():
    sp = get_spotify_client()
    playlist_id = "37i9dQZF1DXcBWIGoYBM5M"  # Example playlist ID for "Top 50 - Global"
    results = sp.playlist_tracks(playlist_id)
    tracks = []
    for track in results['items']:
        # Filter to include only tracks that have a preview URL
        if track['track']['preview_url']:
            track_data = {
                'name': track['track']['name'],
                'artist': track['track']['artists'][0]['name'],
                'id': track['track']['id'],
                'uri': track['track']['uri'],
                'preview_url': track['track']['preview_url']
            }
            tracks.append(track_data)
    return tracks


def trending_music(request):
    artist_name = request.GET.get('artist_name', '')
    category = request.GET.get('category', '')
    country = request.GET.get('country', '')

    # Retrieve trending tracks and filter based on search input
    all_tracks = get_trending_tracks()
    filtered_tracks = []

    for track in all_tracks:
        # Apply search filtering for artist name, category, and country if provided
        artist_match = artist_name.lower() in track['artist'].lower() if artist_name else True
        category_match = category.lower() in track['name'].lower() if category else True
        country_match = country.lower() in track['artist'].lower() if country else True

        if artist_match and category_match and country_match:
            filtered_tracks.append(track)

    # Render the results on the template
    return render(request, 'dashboard/trending_music.html', {'tracks': filtered_tracks})
# views.py



def video_list(request):
    query = request.GET.get('query', 'music')  # Default to 'music' if no query is provided
    videos = search_videos(query)
    
    context = {
        'videos': videos
    }
    return render(request, 'dashboard/video_list.html', context)


def video_list(request):
    youtube = build('youtube', 'v3', developerKey='AIzaSyD4taccS74vlMmAfMpuNI4E9JxLVZdpQ88')

    def get_videos(query, page_token=None):
        request = youtube.search().list(
            part='snippet',
            q=query,
            type='video',
            videoCategoryId='10',  # Music category
            maxResults=10,
            pageToken=page_token
        )
        response = request.execute()
        return response

    query = request.GET.get('query', 'trending music')
    page_token = request.GET.get('page_token', None)
    response = get_videos(query, page_token)

    videos = []
    for item in response.get('items', []):
        video_details = {
            'title': item['snippet']['title'],
            'description': item['snippet']['description'],
            'video_id': item['id']['videoId'],  # Use videoId for embedding
            'video_url': f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        }
        videos.append(video_details)

    next_page_token = response.get('nextPageToken')
    prev_page_token = response.get('prevPageToken')

    context = {
        'videos': videos,
        'next_page_token': next_page_token,
        'prev_page_token': prev_page_token,
        'query': query
    }
    return render(request, 'dashboard/video_list.html', context)
