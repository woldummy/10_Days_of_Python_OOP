# -*- coding: UTF-8 -*-
# we define an abstract base class MediaFile that outlines the structure for different
# types of media files.
# Name: wolke
# Date: 2024-09-03
# macOS: 14.2.1  Python: 3.12


from abc import ABC, abstractmethod

class MediaFile(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def play(self):
        pass