#!/usr/bin/python3
""" contains basiccache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ a caching system that inherists from BaseCaching"""

    def put(self, key, item):
        """assignd key and value to dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """gets key from dictionary"""
        if key:
            return self.cache_data.get(key, None)
