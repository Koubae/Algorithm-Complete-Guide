"""
https://leetcode.com/problems/lru-cache/

https://www.youtube.com/watch?v=XM0eVHfKyF4
"""
import time


class Node:
    def __init__(self, value: int, key: int) -> None:
        self.value: int = value
        self.key: int = key

    def __str__(self):
        return f"Node(k={self.key}, v={self.value}, counter={self.counter})"


class LRUCache:
    def __init__(self, capacity: int):
        self._storage: dict[int, Node] = {}  # key => any
        self._capacity: int = capacity
        self._current_counter: int = 0
        self._lru_map = {}

    def get(self, key: int) -> int:
        node = self._storage.get(key, None)
        if node is None:
            return -1

        self._lru_map[key] = time.time_ns()
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self._storage:
            node = self._storage[key]
            node.value = value
            self._lru_map[key] = time.time_ns()
            return

        self._current_counter += 1
        node = Node(value, key)
        self._storage[key] = node
        self._lru_map[key] = time.time_ns()
        self._evict()

    def _evict(self):
        if self._current_counter <= self._capacity:
            return

        # less = None
        # current_k = None
        # for k, v in self._lru_map.items():
        #     if less is None or v < less:
        #         less = v
        #         current_k = k

        current_k = min(self._lru_map, key=self._lru_map.get)
        if current_k is not None:
            self._current_counter -= 1
            del self._storage[current_k]
            del self._lru_map[current_k]


class NodeV1:
    def __init__(self, value: int, key: int) -> None:
        self.value: int = value
        self.key: int = key
        self.prev: 'NodeV1' | None = None
        self.next: 'NodeV1' | None = None

    def __str__(self):
        prev = True if self.prev else None
        _next = True if self.next else None
        return f"Node(k={self.key}, v={self.value}, prev={prev}, next={_next})"

class LinkedListV1:
    def __init__(self, capacity: int) -> None:
        self.head: NodeV1 | None = None
        self._capacity: int = capacity
        self._current_capacity: int = 0

    def insert_left(self, node: NodeV1):
        self._current_capacity += 1
        if self.head is None:
            self.head = node
            return

            # switchin the head with the new node
        node.next = self.head
        self.head.prev = node
        self.head = node

    def evict(self) -> set[int]:
        if not self.head:
            return set()

        if self._current_capacity <= self._capacity:
            return set()

        capacity = 1
        current = self.head.next
        while current and capacity < self._capacity: # advance
            capacity += 1
            current = current.next

        if current is None:
            return set()
        if current.prev:
            current.prev.next = None

        evicted = set()
        while current:
            evicted.add(current.key)
            current = current.next
            self._current_capacity -= 1
        return evicted

    def promote_node_to_head(self, node: NodeV1) -> None:
        """ remove node from its position and promote to head"""
        if node is self.head:
            return

        if node.prev:
            node.prev.next = node.next              # detach node -> node -> next => previous -> next
        if node.next:
            node.next.prev = node.prev

        node.next = self.head     # node next is current head
        self.head = node          # promote node to head
        self.head.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self._storage: dict[int, NodeV1] = {}  # key => any
        self._lru_tracking: LinkedListV1 = LinkedListV1(capacity=capacity)
        self._capacity: int = capacity

    def get(self, key: int) -> int:
        # increase used count
        node = self._storage.get(key, None)
        if node is None:
            return -1

        self._lru_tracking.promote_node_to_head(node) # remove node from its position and promote to head
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self._storage:
            node = self._storage[key]
            node.value = value
            self._lru_tracking.promote_node_to_head(node)
            return

        node = NodeV1(value, key)

        self._storage[key] = node
        self._lru_tracking.insert_left(node)
        self._evict()

    def _evict(self):
        evicted = self._lru_tracking.evict()
        for key in list(evicted):
            self._storage.pop(key, None)


class NodeSolutionFromNiits:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCacheSolutionFromNiits:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.oldest = NodeSolutionFromNiits(0, 0)
        self.latest = NodeSolutionFromNiits(0, 0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        prev, next = self.latest.prev, self.latest
        prev.next = next.prev = node
        node.next = next
        node.prev = prev

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = NodeSolutionFromNiits(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.oldest.next
            self.remove(lru)
            del self.cache[lru.key]