# -*- coding: UTF-8 -*-
# create concrete implementations of the MediaFile class
# Name: wolke
# Date: 2024-09-03
# macOS: 14.2.1  Python: 3.12
from day5.extension.MediaFile import MediaFile

class AudioFile(MediaFile):
    def play(self):
        return f"Playing audio file: {self.name}"

