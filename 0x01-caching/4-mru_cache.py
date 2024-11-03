#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines an MRU caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.most_recent_key = None

    def put(self, key, item):
        """ Add an item to the cache using MRU
        Args:
            key: the key for the item
            item: the item to add
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.most_recent_key = key
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.most_recent_key in self.cache_data:
                    del self.cache_data[self.most_recent_key]
                    print("DISCARD:", self.most_recent_key)

            self.cache_data[key] = item
            self.most_recent_key = key

    def get(self, key):
        """ Retrieve an item from the cache by key and mark it as recently used
        Args:
            key: the key to look up
        Returns:
            The value associated with key, or None if the key does not exist
        """
        if key in self.cache_data:
            self.most_recent_key = key
            return self.cache_data[key]
        return None
