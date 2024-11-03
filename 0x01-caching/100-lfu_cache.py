#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ LFUCache defines an LFU caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.usage_count = defaultdict(int)
        self.access_order = []

    def put(self, key, item):
        """ Add an item to the cache using LFU with LRU for ties
        Args:
            key: the key for the item
            item: the item to add
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_count[key] += 1
            self._update_access_order(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_key = self._get_lfu_key()
                if lfu_key:
                    del self.cache_data[lfu_key]
                    del self.usage_count[lfu_key]
                    self.access_order.remove(lfu_key)
                    print("DISCARD:", lfu_key)

            self.cache_data[key] = item
            self.usage_count[key] += 1
            self.access_order.append(key)

    def get(self, key):
        """ Retrieve an item from the cache by key and update its usage
        Args:
            key: the key to look up
        Returns:
            The value associated with key, or None if the key does not exist
        """
        if key in self.cache_data:
            self.usage_count[key] += 1
            self._update_access_order(key)
            return self.cache_data[key]
        return None

    def _get_lfu_key(self):
        """ Determine the Least Frequently Used key with LRU tie-breaking """
        min_frequency = min(self.usage_count.values())
        lfu_candidates = [k for k,
                          v in self.usage_count.items() if v == min_frequency]

        if lfu_candidates:
            for key in self.access_order:
                if key in lfu_candidates:
                    return key
        return None

    def _update_access_order(self, key):
        """ Update access order to reflect most recent usage """
        if key in self.access_order:
            self.access_order.remove(key)
        self.access_order.append(key)
