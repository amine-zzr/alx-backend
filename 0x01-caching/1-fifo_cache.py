#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache using FIFO
        Args:
            key: the key for the item
            item: the item to add
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print("DISCARD:", first_key)

    def get(self, key):
        """ Retrieve an item from the cache by key
        Args:
            key: the key to look up
        Returns:
            The value associated with key, or None if the key does not exist
        """
        return self.cache_data.get(key, None)
