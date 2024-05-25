#!/usr/bin/python3
""" BasicCache module """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Adds on the item on the cache

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is not None and item is not None:
            # Assign to the dict self.cache_data the item value for the key key
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key

        Args:
            key (_type_): _description_
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
