# -*- coding: UTF-8 -*-
# using the Media Player class to play different types of media files
# In this system, composition allows the MediaPlayer class to aggregate different types
# of media files, showcasing its flexibility to handle various media types without being
# tightly coupled to their concrete implementations. Abstraction, through the use of
# abstract base classes, ensures that each media type adheres to a common interface,
# allowing the MediaPlayer to interact with them through a unified method (play).
# Name: wolke
# Date: 2024-09-03
# macOS: 14.2.1  Python: 3.12
from day5.extension.AudioFile import AudioFile
from day5.extension.MediaFile import MediaFile
from day5.extension.VideoFile import VideoFile


class MediaPlayer:
    def __init__(self):
        self.playlist = []

    def add_media(self, media_file: MediaFile):
        self.playlist.append(media_file)

    def play_all(self):
        for media in self.playlist:
            print(media.play())

if __name__ == "__main__":
    # Creating instances of media files
    audio1 = AudioFile("song1.mp3")
    video1 = VideoFile("video1.mp4")

    # Creating the media player
    player = MediaPlayer()

    # Adding media files to the player's playlist
    player.add_media(audio1)
    player.add_media(video1)

    # Playing all media in the playlist
    player.play_all()