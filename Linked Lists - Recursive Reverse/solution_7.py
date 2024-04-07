"""
Module contains Node class and one function.
"""

class Node(object):
    """
    Node class."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    """
    Reverses linked list recursively."""
    if not head or not head.next:
        return head
    reversed_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return reversed_head
