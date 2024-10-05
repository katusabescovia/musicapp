// src/spotifyApi.js
import axios from 'axios';
import { getAccessToken } from './SpotifyAuth';

const SPOTIFY_API_URL = 'https://api.spotify.com/v1';

export const fetchPlaylistTracks = async (playlistId) => {
  try {
    const token = await getAccessToken();
    const response = await axios.get(`${SPOTIFY_API_URL}/playlists/${playlistId}/tracks`, {
      headers: {
        'Authorization': `Bearer ${token}`,
      },
    });
    return response.data.items;
  } catch (error) {
    console.error('Error fetching playlist tracks:', error);
    return [];
  }
};

// Other API functions...
