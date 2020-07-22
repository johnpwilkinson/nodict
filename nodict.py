#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'John, stackOverFlow, and programwiz, Daniels Demo on 7/14'


class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.hash = hash(self.key)

    def __repr__(self):
        """returns contents in a human readable format"""
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """allows for the comparison 
        of node objects to the node class"""
        return self.key == other.key



class NoDict:
    def __init__(self, num_buckets=10):
        """initializes buckets... the deafult bucket count is 10"""
        self.buckets = [[] for el in range(num_buckets)]
        self.size = num_buckets

    def __repr__(self):
        """ returns a string representing the contents of NoDict"""
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}'
                            for i,bucket in enumerate(self.buckets)])

    def add(self, key, value=None):
        """adds a new entry to a NoDict bucket"""
        new_node = Node(key, value)
        bucket = self.buckets[new_node.hash % self.size]
        for key_value in bucket:
            if key_value == new_node:
                bucket.remove(key_value)
                break
        bucket.append(new_node)

    def get(self, key):
        """gets key/val pair"""
        key_value = Node(key)
        bucket = self.buckets[key_value.hash % self.size]
        for key_val in bucket:
            if key_val == key_value:
                return key_val.value
        raise KeyError(f'{key} was not found')

    def __getitem__(self, key):
        """gets NoDict entry and imitates the square bracket functionality"""
        return self.get(key)

    def __setitem__(self, key, value):
        """sets the value of a key/val pair by imitating square bracket notation"""
        self.add(key, value)
