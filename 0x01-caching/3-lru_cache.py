#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines an LRU caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """ Add an item to the cache using LRU
        Args:
            key: the key for the item
            item: the item to add
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.access_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.access_order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)

            self.cache_data[key] = item
            self.access_order.append(key)

    def get(self, key):
        """ Retrieve an item from the cache by key and mark it as recently used
        Args:
            key: the key to look up
        Returns:
            The value associated with key, or None if the key does not exist
        """
        if key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None
