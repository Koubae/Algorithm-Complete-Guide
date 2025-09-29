# noinspection DuplicatedCode
"""
Binary Search -- Depth First Search (DFS)
"""
import typing as t
from collections import deque
from dataclasses import dataclass, field


@dataclass
class Node:
    value: t.Any
    left: t.Self | None = field(default=None)
    right: t.Self | None = field(default=None)


@dataclass
class Tree:
    root: Node | None = field(default=None)

    def find_dfs_iterative(self, target: t.Any) -> Node | None:
        """Preorder Root --> left --> right"""
        if self.root is None:
            return None

        found: Node | None = None
        stack = deque([self.root])  # LIFO queue
        while stack and not found:
            current = stack.pop()

            if current.value == target:
                found = current
                break

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return found

    def find_dfs_recursevely(self, target: t.Any) -> Node | None:
        """Preorder Root --> left --> right"""
        if self.root is None:
            return None

        found: Node | None = None

        def _recursive(node: Node | None) -> None:
            nonlocal found

            if node is None:
                return
            if found is not None:
                return

            if node.value == target:
                found = node
                return

            _recursive(node.left)
            if found is not None:
                return
            _recursive(node.right)

        _recursive(self.root)
        return found

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

    targets = (
        (1, True),
        (7, True),
        (30, True),
        (11, True),
        (24, True),
        (99, False),
        (-1, False),
        (150, False),
        (4, True),
        (8, True)
    )

    for target, expected in targets:
        found = tree_huge.find_dfs_iterative(target)
        assert_found_value(expected, found, target)

    for target, expected in targets:
        found = tree_huge.find_dfs_recursevely(target)
        assert_found_value(expected, found, target)


def assert_found_value(expected: bool, found: Node | None, target: int):
    found_value = found.value if found else None
    target_value = target if expected else None

    assert bool(found) == expected, f"Target {target} should be {expected} got: {found}"
    assert found_value == target_value, f"Target {target} should be {target_value} got: {found_value}"


if __name__ == '__main__':
    main()
