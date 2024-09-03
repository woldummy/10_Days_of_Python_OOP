# -*- coding: UTF-8 -*-
# Using DataProcessor and its subclasses
# Name: wolke
# Date: 2024-09-03
# macOS: 14.2.1  Python: 3.12
from day5.DataProcessor import DataProcessor
from day5.ImageProcessor import ImageProcessor
from day5.TextProcessor import TextProcessor

if __name__ == "__main__":
    image_processor = ImageProcessor("path/to/image/data")
    image_processor.load_data() # Inherited method
    image_processor.process_data() # Subclass-specific method
    text_processor = TextProcessor("path/to/text/data")
    text_processor.load_data() # Inherited method
    text_processor.process_data() # Subclass-specific method
    image_processor.show_data()
