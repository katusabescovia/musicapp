import React, { createContext, useState, useContext, useRef, useEffect } from 'react';

const AudioContext = createContext();

export const AudioProvider = ({ children }) => {
  const [currentSong, setCurrentSong] = useState(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [progress, setProgress] = useState(0);
  const audioRef = useRef(new Audio());

  useEffect(() => {
    const audio = audioRef.current;
    const updateProgress = () => {
      setProgress((audio.currentTime / audio.duration) * 100);
    };

    audio.addEventListener('timeupdate', updateProgress);
    return () => audio.removeEventListener('timeupdate', updateProgress);
  }, []);

  const playSong = (song) => {
    const audio = audioRef.current;
    if (currentSong && currentSong.id === song.id) {
      if (isPlaying) {
        audio.pause();
        setIsPlaying(false);
      } else {
        audio.play();
        setIsPlaying(true);
      }
    } else {
      if (currentSong) {
        audio.pause();
      }
      audio.src = song.audio_url;
      audio.play();
      setCurrentSong(song);
      setIsPlaying(true);
    }
  };

  const seekTo = (percent) => {
    const audio = audioRef.current;
    audio.currentTime = (percent / 100) * audio.duration;
  };

  return (
    <AudioContext.Provider value={{ currentSong, isPlaying, progress, playSong, seekTo }}>
      {children}
    </AudioContext.Provider>
  );
};

export const useAudio = () => useContext(AudioContext);