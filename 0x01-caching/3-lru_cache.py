#!/usr/bin/env python3

""" Least Recently Used caching approach """

# from base_caching import BaseCaching
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ A cache using the LRU approach. """
    def __init__(self):
        """ Initializes the cache. """
        super().__init__()
        self.track_usage = []

    def put(self, key, item):
        """ Adds item into cache """
        if not key or not item:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.track_usage[0]))
            del self.cache_data[self.track_usage[0]]
            del self.track_usage[0]
        if key in self.track_usage:
            del self.track_usage[self.track_usage.index(key)]
        self.track_usage.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Getting an item from the cache. """
        if not key or key not in self.cache_data:
            return None
        del self.track_usage[self.track_usage.index(key)]
        self.track_usage.append(key)
        return self.cache_data[key]
