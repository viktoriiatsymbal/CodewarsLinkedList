"""
Module contains Node class and two functions.
"""

class Node:
    """
    Node class."""
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    """
    The function creates a new linked list/node."""
    return Node(data, head)

def build_one_two_three():
    pass
