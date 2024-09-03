# -*- coding: UTF-8 -*-
# TextProcessor inherits from DataProcessor
# Name: wolke
# Date: 2024-09-03
# macOS: 14.2.1  Python: 3.12
from day5.DataProcessor import DataProcessor


class TextProcessor(DataProcessor):

    def process_data(self):
        print("Processing text data...")
        # Text-specific processing logic
