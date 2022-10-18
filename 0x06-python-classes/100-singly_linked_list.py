#!/usr/bin/python3
""" Define class"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(value):
        return (self.__data)

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")
    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if value or value == None:
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")



