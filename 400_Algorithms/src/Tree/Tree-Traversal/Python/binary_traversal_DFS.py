# noinspection DuplicatedCode
"""
Binary Traversal -- Depth First Search (DFS)
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

    def traverse_dfs_iterative(self) -> list[Node]:
        """Preorder Root --> left --> right"""
        visited: list[Node] = []
        if self.root is None:
            return visited

        stack = deque([self.root])
        while stack:

            node = stack.pop()
            visited.append(node)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return visited

    def traverse_dfs_recursevely(self) -> list[Node]:
        """Preorder Root --> left --> right"""
        visited: list[Node] = []
        if self.root is None:
            return visited

        def _traverse(node: Node | None):
            if node is None:
                return

            visited.append(node)

            _traverse(node.left)
            _traverse(node.right)

        _traverse(self.root)
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

    traversal_iter = tree_huge.traverse_dfs_iterative()
    traversal_recursive = tree_huge.traverse_dfs_recursevely()

    print(f"Traversal Iterative: {traversal_iter}")
    print(f"Traversal Recursive: {traversal_recursive}")

    check = [
        1, 2, 4, 8, 16, 17, 9, 18, 19, 5, 10, 20, 21, 11, 22, 23,
        3, 6, 12, 24, 25, 13, 26, 27, 7, 14, 28, 29, 15, 30, 31
    ]
    assert [node.value for node in traversal_iter] == check, f"Expected {check} got {traversal_iter}"


if __name__ == '__main__':
    main()
