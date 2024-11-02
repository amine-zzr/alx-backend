#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines a basic caching system with no limit """

    def put(self, key, item):
        """ Add an item to the cache
        Args:
            key: the key for the item
            item: the item to add
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache by key
        Args:
            key: the key to look up
        Returns:
            The value associated with key, or None if the key does not exist
        """
        return self.cache_data.get(key, None)
