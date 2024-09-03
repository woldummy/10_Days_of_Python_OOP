# -*- coding: UTF-8 -*-
# Base class Data Prcessor
# Name: wolke
# Date: 2024-09-03
# macOS: 14.2.1  Python: 3.12
from abc import abstractmethod


class DataProcessor:
    def __init__(self, data_source):
        self.data_source = data_source

    def load_data(self):
        """Implementation to load data"""
        print(f"Loading data from {self.data_source}")

    def save_data(self, data):
        # Implementation to save data
        print("Saving data...")

    def show_data(self):
        # Implementation to display data
        print("Displaying data...")

    @abstractmethod
    def process_data(self):
        pass
