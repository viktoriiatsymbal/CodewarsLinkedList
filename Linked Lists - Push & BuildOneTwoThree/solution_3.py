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
    if head is None:
        return Node(data)
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    pass
