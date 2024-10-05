import React, { useState, useEffect, useRef } from 'react';
import { fetchPlaylistTracks } from './SpotifyApi';
import '../components/Library.css';
import { FaPlus, FaDownload, FaShare, FaPlay, FaMusic } from 'react-icons/fa'; // Importing icons from react-icons

const Library = () => {
  const [tracks, setTracks] = useState([]);
  const [currentTrackIndex, setCurrentTrackIndex] = useState(null);
  const [showAddPlaylistPopup, setShowAddPlaylistPopup] = useState(false);
  const [privatePlaylists, setPrivatePlaylists] = useState([]);
  const [newPlaylistName, setNewPlaylistName] = useState('');
  const [selectedTrack, setSelectedTrack] = useState(null);
  const [searchQuery, setSearchQuery] = useState(''); // State for search query
  const audioRef = useRef(null);

  useEffect(() => {
    const loadPlaylist = async () => {
      const playlistId = '37i9dQZF1DWTwnEm1IYyoj'; // Your Spotify playlist ID
      const fetchedTracks = await fetchPlaylistTracks(playlistId);
      setTracks(fetchedTracks);
    };

    loadPlaylist();
  }, []);

  const playTrack = (index) => {
    if (index === currentTrackIndex) {
      return; // Do nothing if the same track is requested
    }

    setCurrentTrackIndex(index);

    const newTrack = tracks[index].track;
    if (audioRef.current) {
      if (newTrack.preview_url) {
        audioRef.current.pause(); // Pause the currently playing track
        audioRef.current.src = newTrack.preview_url; // Change the source to the new track
        audioRef.current.load(); // Load the new track
        audioRef.current.play(); // Start playing the new track
      } else {
        console.error('Preview URL is not available for this track');
        // Handle cases where the preview URL is not available
      }
    }
  };

  const handleNextTrack = () => {
    if (currentTrackIndex < tracks.length - 1) {
      playTrack(currentTrackIndex + 1);
    }
  };

  const handlePreviousTrack = () => {
    if (currentTrackIndex > 0) {
      playTrack(currentTrackIndex - 1);
    }
  };

  const handleAddToPlaylist = (track) => {
    setSelectedTrack(track);
    setShowAddPlaylistPopup(true);
  };

  const handleCreatePlaylist = () => {
    if (newPlaylistName) {
      setPrivatePlaylists([...privatePlaylists, { name: newPlaylistName, tracks: [] }]);
      setNewPlaylistName('');
      setSelectedTrack(null);
      setShowAddPlaylistPopup(false);
    }
  };

  const handleAddTrackToPlaylist = () => {
    if (selectedTrack && privatePlaylists.length > 0) {
      const updatedPlaylists = [...privatePlaylists];
      let added = false;

      for (let i = 0; i < updatedPlaylists.length; i++) {
        if (updatedPlaylists[i].tracks.length < 100) {
          updatedPlaylists[i].tracks.push(selectedTrack);
          added = true;
          break;
        }
      }

      if (!added) {
        // If no existing playlist can take the track, create a new playlist
        setPrivatePlaylists([...updatedPlaylists, { name: `Playlist ${updatedPlaylists.length + 1}`, tracks: [selectedTrack] }]);
      } else {
        setPrivatePlaylists(updatedPlaylists);
      }
      setSelectedTrack(null);
      setShowAddPlaylistPopup(false);
    }
  };

  const handleDownloadTrack = (track) => {
    const link = document.createElement('a');
    link.href = track.preview_url; // This assumes preview_url can be used for download; otherwise, you need a valid download URL
    link.download = `${track.name}.mp3`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const handleShareTrack = (track) => {
    const link = track.external_urls.spotify;
    navigator.clipboard.writeText(link);
    alert('Link copied to clipboard!');
  };

  const handlePlayTrackFromPlaylist = (track) => {
    const index = tracks.findIndex(t => t.track.id === track.id);
    playTrack(index);
  };

  // Filter tracks based on search query
  const filteredTracks = tracks.filter((item) => 
    item.track.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    item.track.artists[0].name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const currentTrack = tracks[currentTrackIndex];

  const handleCancelCreatePlaylist = () => {
    setNewPlaylistName('');
    setSelectedTrack(null);
    setShowAddPlaylistPopup(false); // Hide the popup when canceling
  };

  return (
    <div className="library-page">
      <header className="header">
        <h1>Library</h1>
        <FaMusic className="music-icon" /> {/* Updated to use react-icons */}
        {/* Search Bar */}
        <input
          type="text"
          placeholder="Search..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="search-bar"
        />
      </header>
      <section className="now-playing">
        {currentTrack && (
          <div className="now-playing-info">
            <img src={currentTrack.track.album.images[0].url} alt={currentTrack.track.name} className="album-cover" />
            <div className="track-info">
              <h2 className="track-title">{currentTrack.track.name}</h2>
              <h3 className="track-artist">{currentTrack.track.artists[0].name}</h3>
              <p className="track-duration">{formatDuration(currentTrack.track.duration_ms)}</p>
              <audio ref={audioRef} controls onEnded={handleNextTrack}>
                <source src={currentTrack.track.preview_url} type="audio/mpeg" />
                Your browser does not support the audio element.
              </audio>
            </div>
            <div className="controls">
              <button onClick={handlePreviousTrack} className="control-button">Previous</button>
              <button onClick={() => audioRef.current.paused ? audioRef.current.play() : audioRef.current.pause()} className="control-button">
                {audioRef.current && audioRef.current.paused ? 'Play' : 'Pause'}
              </button>
              <button onClick={handleNextTrack} className="control-button">Next</button>
            </div>
          </div>
        )}
      </section>
      <section className="playlist">
        <h2>Playlist</h2>
        <ul className="playlist-carousel">
          {filteredTracks.map((item, index) => (
            <li key={index} className={`playlist-item ${index === currentTrackIndex ? 'active' : ''}`} onClick={() => playTrack(index)}>
              <img src={item.track.album.images[0].url} alt={item.track.name} className="playlist-album-cover" />
              <div className="playlist-track-info">
                <h3>{item.track.name}</h3>
                <p>{item.track.artists[0].name}</p>
              </div>
              <div className="playlist-controls">
                <button onClick={() => handleAddToPlaylist(item.track)} className="playlist-control-button">
                  <FaPlus />
                </button>
                <button onClick={() => handleDownloadTrack(item.track)} className="playlist-control-button">
                  <FaDownload />
                </button>
                <button onClick={() => handleShareTrack(item.track)} className="playlist-control-button">
                  <FaShare />
                </button>
              </div>
            </li>
          ))}
        </ul>
      </section>
      <section className="private-playlists">
        <h2>My Playlists</h2>
        <ul>
          {privatePlaylists.map((playlist, index) => (
            <li key={index} className="playlist-folder">
              <h3>{playlist.name}</h3>
              <ul className="playlist-tracks">
                {playlist.tracks.map((track, trackIndex) => (
                  <li key={trackIndex} className="playlist-item">
                    <span>{track.name}</span>
                    <button onClick={() => handlePlayTrackFromPlaylist(track)} className="playlist-control-button">
                      <FaPlay />
                    </button>
                  </li>
                ))}
              </ul>
            </li>
          ))}
        </ul>
      </section>
      {showAddPlaylistPopup && (
        <div className="add-to-playlist-popup">
          <div className="popup-content">
            <h3>Create New Playlist</h3>
            <input
              type="text"
              value={newPlaylistName}
              onChange={(e) => setNewPlaylistName(e.target.value)}
              placeholder="Playlist Name"
            />
            <button onClick={handleCreatePlaylist}>Create</button>
            <button onClick={handleAddTrackToPlaylist}>Add to Playlist</button>
            <button onClick={handleCancelCreatePlaylist}>Cancel</button> {/* Added Cancel button */}
          </div>
        </div>
      )}
    </div>
  );
};

// Function to format the track duration from milliseconds to minutes and seconds
const formatDuration = (duration) => {
  const minutes = Math.floor(duration / 60000);
  const seconds = Math.floor((duration % 60000) / 1000);
  return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
};

export default Library;
