"""
Module contains Node class and two functions (one of them is nested)."""

class Node():
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    """
    Gets Nth node."""
    def get_len(node):
        """
        Gets length of the node."""
        length = 0
        current = node
        while current:
            length += 1
            current = current.next
        return length

    current = node
    index_counter = -1
    if node is not None:
        if 0<= index <= get_len(node) - 1:
            while current:
                index_counter += 1
                if index_counter == index:
                    return current
                current = current.next
        raise ValueError("Invalid index value should throw error.")
    raise ValueError("None linked list should throw error.")
