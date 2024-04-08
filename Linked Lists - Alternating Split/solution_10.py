"""
Module contains Node and Context classes and one function.
"""

class Node(object):
    """
    Node class."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    """
    Context class."""
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """
    Creates linked list by splitting list into alternating elements."""
    if not head or not head.next:
        raise Exception
    first_head = head
    second_head = head.next
    first_curr = first_head
    second_curr = second_head
    while first_curr.next and second_curr.next:
        first_curr.next = second_curr.next
        first_curr = first_curr.next
        second_curr.next = first_curr.next
        second_curr = second_curr.next
    first_curr.next = None
    return Context(first_head, second_head)
