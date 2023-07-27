#!/usr/bin/env python3

""" FIFO caching. """

# from base_caching import BaseCaching
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        """ Initializes the cache. """
        super().__init__()
        self.track_order = []

    def put(self, key, item):
        """ Adds item into cache """
        if not key or not item:
            return
        self.track_order.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.track_order[0]))
            del self.cache_data[self.track_order[0]]
            del self.track_order[0]

    def get(self, key):
        """ Getting an item from the cache. """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
