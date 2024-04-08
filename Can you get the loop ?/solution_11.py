"""
Module contains one function."""

def loop_size(node):
    """
    Determines the length of the loop."""
    nodes_set = set()
    len_counter = 0
    while node:
        if node in nodes_set:
            current = node
            while True:
                len_counter += 1
                current = current.next
                if current == node:
                    break
            return len_counter
        nodes_set.add(node)
        node = node.next
    return len_counter
