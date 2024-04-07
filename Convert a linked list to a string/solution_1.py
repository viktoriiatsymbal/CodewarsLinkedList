"""
Contains function that converts a linked list to a string."""
class Node():
    """
    Node class."""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node: 'Node'):
    res = ""
    while node is not None:
        res += str(node.data)
        res += " -> "
        node = node.next
    return res + "None"
