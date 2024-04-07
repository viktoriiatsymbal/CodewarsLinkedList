"""
Module contains Node class and one function."""
class Node(object):
    """
    Node class."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """
    Context class."""
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """
    Moves which takes front source node and moves it to the front of the destintation list.
    """
    if not source:
        raise Exception
    if not dest:
        dest = Node(source.data)
        source = source.next
        return Context(source, dest)
    current_data = source.data
    dest = push(dest, current_data)
    if not source.next:
        source = None
    else:
        source = source.next
    return Context(source, dest)
