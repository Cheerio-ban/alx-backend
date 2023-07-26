#!/usr/bin/env python3

""" A basic dictionary using a class """

# from base_caching import BaseCaching
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ A basic cache class. """
    def __init__(self):
        """ Initializes the class based on the super class. """
        super().__init__()

    def put(self, key, item):
        """ Adds an item to the dictionary """
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Gets value stored at a particular key. """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
