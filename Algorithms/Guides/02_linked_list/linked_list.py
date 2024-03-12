class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes  - data and link to the next node in the list
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"


class LinkedList:
    """
    Singly Linked list
    """

    def __init__(self):
        self.head = None

    def __repr__(self):

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")

            current = current.next_node

        return "-> ".join(nodes)

    def is_empty(self) -> bool:
        return bool(self.head)

    def size(self):

        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node

        return count

    def search(self, search_value):
        """
        Complexity O(n)
        Args:
            search_value ():

        Returns:

        """
        current = self.head

        while current:
            if current.data == search_value:
                return current
            current = current.next_node
        return None

    def add(self, data):
        """
        Complexity O(n)
        Adds new NOde containing data at the head of the list
        Args:
            data ():

        Returns:

        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node



if __name__ == '__main__':
    l = LinkedList()
    for i in range(10):
        l.add(i)

    print(l)
    print(l.search(5))