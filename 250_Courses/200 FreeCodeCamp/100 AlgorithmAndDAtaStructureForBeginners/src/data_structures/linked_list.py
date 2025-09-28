import typing as t
from dataclasses import dataclass


@dataclass
class Node:
    data: int
    next: t.Self | None = None

    def __str__(self) -> str:
        next_value = id(self.next) if self.next else None
        return f"Node(data={self.data}, next={next_value})"


class LinkedList:
    def __init__(self, head: Node) -> None:
        self.head: Node = head

    def __str__(self) -> str:
        return f"LinkedList(head={self.head}, size={self.size()})"

    def __repr__(self) -> str:
        return f"LinkedList(size={self.size()}, linked_list={self.show()})"

    def insert(self, data: int) -> tuple[int, Node]:
        i = 0
        current = self.head
        while current.next:
            i += 1
            current = current.next

        node = Node(data)
        current.next = node
        return i, node

    def insert_first(self, data: int) -> Node:
        node = Node(data)
        node.next = self.head
        self.head = node
        return node

    def insert_at(self, data: int, index: int) -> Node:
        if index == 0:
            node = self.insert_first(data)
            return node

        i = 1
        previous = self.head
        current = self.head.next
        while current:
            if i == index:
                break

            previous = current
            current = previous.next
            i += 1

        node = Node(data)
        previous.next = node
        node.next = current
        return node

    def remove(self, data: int) -> bool:
        current = self.head
        previous = None
        found = False
        while current:
            if current.data != data:
                previous = current
                current = current.next
                continue

            found = True
            if current is self.head:
                del self.head
                self.head = current.next
                break

            previous.next = current.next
            del current
            break

        return found

    def size(self) -> int:
        current = self.head
        i = int(bool(current))
        while i and current.next:
            i += 1
            current = current.next
        return i

    def sort(self) -> None:
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head: Node) -> Node | None:
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow
        middle_right = middle.next
        middle.next = None # Break linked-list

        left = self._merge_sort(head)
        right = self._merge_sort(middle_right)

        # Merge sorted halves
        return self._sorted_merge(left, right)

    def _sorted_merge(self, a, b):
        """Merge two sorted linked lists."""
        if not a:
            return b
        if not b:
            return a
        if a.data <= b.data:
            result = a
            result.next = self._sorted_merge(a.next, b)
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)
        return result

    def traverse(self) -> t.Generator[tuple[int, Node], None, None]:
        i = 0
        current = self.head
        if current is None:
            return
        yield i, current
        while current and current.next:
            i += 1
            current = current.next
            yield i, current
        return

    def show(self, as_tree: bool = False) -> str:
        if not self.head:
            return "Empty list"

        linked_list = f"[{self.head.data}"
        current = self.head.next
        i = 0
        while current:
            i += 1
            if as_tree:
                tabs = '  ' * i
                linked_list += f"\n{tabs} -> {current.data}"
            else:
                linked_list += f", {current.data}"
            current = current.next

        linked_list += "]"
        return linked_list


def main():
    linked_list = LinkedList(Node(200))

    linked_list.insert(100)
    linked_list.insert(20)
    linked_list.insert(4)
    linked_list.insert(300)
    linked_list.insert(8)
    linked_list.insert(999)
    linked_list.insert(23)

    print(linked_list)
    print(f"Traversing the linked list:")
    for i, node in linked_list.traverse():
        print(f"{i}: {node}")

    print(repr(linked_list))
    print(linked_list.show(as_tree=True))

    linked_list.insert_first(1000)
    linked_list.insert_first(2520)
    linked_list.insert_first(99)
    print(repr(linked_list))

    linked_list.insert_at(10000, 0)
    print(f"Inserted 10000 at 0")
    print(repr(linked_list))
    linked_list.insert_at(123, 1)
    print(f"Inserted 123 at 1")
    print(repr(linked_list))
    linked_list.insert_at(33, 4)
    print(f"Inserted 33 at 4")
    print(repr(linked_list))

    last_index = linked_list.size()
    node = linked_list.insert_at(777, last_index)
    print(f"Inserted 777 at {last_index}")
    print(repr(linked_list))
    print(f"Last node: {node}")

    removed = linked_list.remove(10000)
    print(f"Removed 10000: {removed}")
    print(repr(linked_list))

    removed = linked_list.remove(777)
    print(f"Removed 777: {removed}")
    print(repr(linked_list))


    removed = linked_list.remove(33)
    print(f"Removed 33: {removed}")
    print(repr(linked_list))

    print("Sort Linked list")
    linked_list.sort()
    print(repr(linked_list))

    items = [node for _, node in linked_list.traverse()]
    print(f"Delete All items from linked list (from tail to head) -- items : {items}")

    for node in items[::1]:
        removed = linked_list.remove(node.data)
        print(f"Removed {node.data}: {removed}")
        print(repr(linked_list))

    removed = linked_list.remove(123)
    print(f"Removed 123: {removed}")

    print("Result")
    print(repr(linked_list))

if __name__ == '__main__':
    main()
