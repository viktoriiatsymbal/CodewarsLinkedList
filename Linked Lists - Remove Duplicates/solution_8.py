"""
Module contains Node class and one function.
"""

class Node(object):
    """
    Node class."""
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    """
    Removes duplicates from linked list."""
    if not head:
        return None
    if not head.next:
        return head
    new_head = Node(head.data)
    current = new_head
    head = head.next
    while head:
        if head.data != current.data:
            current.next = Node(head.data)
            current = current.next
        head = head.next
    return new_head
