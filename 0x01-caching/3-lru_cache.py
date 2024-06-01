#!/usr/bin/python3
""" LRU cache module """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU cache class

    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self):
        """ Initiliaze the dictionary from parent class"""
        super().__init__()
    
    def put(self, key, item):
        """ Add an item in the cache

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # get the least recently used key in the cache dict
                pop_least_recently_used_key = self.cache_data.popitem(last=False)
                print("DISCARD: {}".format(pop_least_recently_used_key[0]))
                self.cache_data[key] = item


    def get(self, key):
        """ Get an item by key

        Args:
            key (_type_): _description_
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]