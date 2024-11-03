#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a LIFO caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item to the cache using LIFO
        Args:
            key: the key for the item
            item: the item to add
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last_key in self.cache_data:
                    del self.cache_data[self.last_key]
                    print("DISCARD:", self.last_key)
            self.last_key = key

    def get(self, key):
        """ Retrieve an item from the cache by key
        Args:
            key: the key to look up
        Returns:
            The value associated with key, or None if the key does not exist
        """
        return self.cache_data.get(key, None)
