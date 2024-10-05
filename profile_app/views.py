from django.shortcuts import render


# Create your views here.
def profile(request):
    return render(request, "profile/profile.html")




# def edit_profile(request):
#     return render(request, 'musicApp/edit_profile.html')

def downloads(request):
    return render(request, 'profile/downloads.html')

def albums(request):
    return render(request, 'profile/albums.html')

def playlists(request):
    return render(request, 'profile/playlists.html')

def favorites(request):
    return render(request, 'profile/favourites.html')
