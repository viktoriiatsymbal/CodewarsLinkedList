"""
Module contains Node class and one function."""

class Node(object):
    """
    Node class."""
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    """
    Places data into sorted linked list."""
    node = Node(data)
    if head is None or data < head.data:
        node.next = head
        return node
    current = head
    while current.next is not None and current.next.data < data:
        current = current.next
    node.next = current.next
    current.next = node
    return head
  
