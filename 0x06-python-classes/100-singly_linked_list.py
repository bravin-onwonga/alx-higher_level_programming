#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')

        self.__data = value

    @property
    def data(self):
        return self.__data

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value

    @property
    def next_node(self):
        return self.__next_node

class SinglyLinkedList:
    def __init__(self, head):
        self.__head = head

    def sorted_insert(self, value):
        new_node = Node()


