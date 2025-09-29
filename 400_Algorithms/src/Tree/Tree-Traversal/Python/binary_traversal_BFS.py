# noinspection DuplicatedCode
"""
Binary Traversal -- Breadth First Search (BFS)
"""
import typing as t
from collections import deque
from dataclasses import dataclass, field


@dataclass
class Node:
    value: t.Any
    left: t.Self | None = field(default=None)
    right: t.Self | None = field(default=None)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


@dataclass
class Tree:
    root: Node | None = field(default=None)

    def traverse_bfs(self) -> list[Node]:
        """Level-Order"""
        visited: list[Node] = []
        queue = deque([self.root])  # |.............=>
        while queue:

            node = queue.pop()
            visited.append(node)

            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)

        return visited


def main():
    tree_huge = Tree(
        root=Node(1,
            left=Node(2,
                left=Node(4,
                    left=Node(8,
                        left=Node(16),
                        right=Node(17),
                    ),
                    right=Node(9,
                        left=Node(18),
                        right=Node(19),
                    ),
                ),
                right=Node(5,
                    left=Node(10,
                        left=Node(20),
                        right=Node(21),
                    ),
                    right=Node(11,
                        left=Node(22),
                        right=Node(23),
                    ),
                ),
            ),
            right=Node(3,
                left=Node(6,
                    left=Node(12,
                        left=Node(24),
                        right=Node(25),
                    ),
                    right=Node(13,
                        left=Node(26),
                        right=Node(27),
                    ),
                ),
                right=Node(7,
                    left=Node(14,
                        left=Node(28),
                        right=Node(29),
                    ),
                    right=Node(15,
                        left=Node(30),
                        right=Node(31),
                    ),
                ),
            ),
        ),
    )

    traversal_bfs = tree_huge.traverse_bfs()

    print(f"Traversal (BFS): {traversal_bfs}")

    check = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31
    ]
    assert [node.value for node in traversal_bfs] == check, f"Expected {check} got {traversal_bfs}"


if __name__ == '__main__':
    main()
