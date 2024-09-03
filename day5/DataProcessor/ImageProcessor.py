# -*- coding: UTF-8 -*-
# ImageProcessor inherits from DataProcessor
# Name: wolke
# Date: 2024-09-03
# macOS: 14.2.1  Python: 3.12
from day5.DataProcessor import DataProcessor


class ImageProcessor(DataProcessor):

    def process_data(self):
        print("Processing image data...") # Image-specific processing logic

    def show_data(self):
        super().show_data()
        print("Displaying the image")