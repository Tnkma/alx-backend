#!/usr/bin/python3
""" LIFOCache cache module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache cache class

    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self):
        """ Initiliaze the dictionary from parent class"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache

        Args:
            key (_type_): the key for the cache
            item (_type_): the item for the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # get the first key in the cache dict
                last_key = list(self.cache_data.keys())[-1]
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))
            self.cache_data[key] = item

    def get(self, key):
        """ Gets the items by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
