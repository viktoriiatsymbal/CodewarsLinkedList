"""
Contains function that parses a linked list from a string."""
class Node:
    """
    Node class."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s: str):
    """
    Parses a linked list from a string."""
    s = s.split(" -> ") # ['1', '2', '3', 'None']
    if s[0] == "None":
        return None
    if s[0] == "0":
        head = Node(0)
    else:
        head = Node(int(s[0]))
    current = head
    for data in s[1:]:
        if data != "None":
            current.next = Node(int(data))
            current = current.next
    return head
