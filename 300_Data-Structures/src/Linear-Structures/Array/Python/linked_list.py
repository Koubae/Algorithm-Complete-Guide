"""
    Deque Implementations in Python
    @Author: Federico Baù
    @Creation Date: 20 - Jan - 2021
    @Updated: N/a
    
"""


# ========================= < Linked-list > ========================= #

# ----------- Node
class Node:
    """A node of a linked list"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        """Get node data"""
        return self._data

    def set_data(self, node_data):
        """Set node data"""
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        """Get next node"""
        return self._next

    def set_next(self, node_next):
        """Set next node"""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        """String"""
        return str(self._data)


# -------------- Unordered List
# NOTE: the list class itself does not contain any node objects. Instead it contains a single reference to only the first node in the linked structure.
class UnorderedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp


def size(self):
    """Using a traversal Technique"""
    current = self.head
    count = 0
    while current is not None:
        count = count + 1
        current = current.next

    return count


def search(self, item):
    """Using a traversal Technique"""
    current = self.head
    while current is not None:
        if current.data == item:
            return True
        current = current.next

    return False


def remove(self, item):
    current = self.head
    previous = None

    while current is not None:
        if current.data == item:
            break
        previous = current
        current = current.next

    if current is None:
        raise ValueError("{} is not in the list".format(item))
    if previous is None:
        self.head = current.next
    else:
        previous.next = current.next


my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)


# ----------- Node
class Node:
    """A node of a linked list"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        """Get node data"""
        return self._data

    def set_data(self, node_data):
        """Set node data"""
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        """Get next node"""
        return self._next

    def set_next(self, node_next):
        """Set next node"""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        """String"""
        return str(self._data)


# -------------- Ordered List
class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            if current.data > item:
                return False
            current = current.next

        return False

    def add(self, item):

        """Add a new node"""
    current = self.head
    previous = None
    temp = Node(item)

    while current is not None and current.data < item:
        previous = current
        current = current.next

    if previous is None:
        temp.next = self.head
        self.head = temp
    else:
        temp.next = current
        previous.next = temp
