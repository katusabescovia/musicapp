from googleapiclient.discovery import build

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'AIzaSyD4taccS74vlMmAfMpuNI4E9JxLVZdpQ88'

def get_youtube_client():
    return build('youtube', 'v3', developerKey=api_key)
def search_videos(query, max_results=5):
    youtube = get_youtube_client()
    request = youtube.search().list(
        part='snippet',
        q=query,
        type='video',
        maxResults=max_results
    )
    response = request.execute()
    return response.get('items', [])
