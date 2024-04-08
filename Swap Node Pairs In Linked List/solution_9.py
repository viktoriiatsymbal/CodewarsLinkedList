"""
Module contains Node class and one function.
"""
class Node:
    """
    Node class."""
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    """
    Swaps pairs in linked list that not contains any data."""
    basic_node = Node()
    basic_node.next = head
    prev = basic_node
    while prev.next and prev.next.next:
        first_node = prev.next
        second_node = prev.next.next
        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node
        prev = first_node
    return basic_node.next
