# noinspection DuplicatedCode
"""https://leetcode.com/problems/invert-binary-tree/description/"""
import typing as t
from dataclasses import dataclass, field


@dataclass
class Node:
    value: t.Any
    left: t.Self | None = field(default=None)
    right: t.Self | None = field(default=None)


@dataclass
class Tree:
    root: Node | None = field(default=None)

    def __str__(self):
        tree = f"Tree(root={self.root.value}"

        collect = self.traverse()
        tree += f" {str(collect)}"
        return tree

    def __eq__(self, other: t.Self | t.Any) -> bool:
        if not other:
            return False
        if not isinstance(other, Tree):
            return False

        def _equal(root_a: Node | None, root_b: Node | None) -> bool:
            if root_a is None or root_b is None:
                return root_a == root_b

            if root_a.value != root_b.value:
                return False

            return _equal(root_a.left, root_b.left) and _equal(root_a.right, root_b.right)

        return _equal(self.root, other.root)

    def invert(self):
        def _invert(root: Node | None) -> None:
            if root is None:
                return

            root.left, root.right = root.right, root.left
            _invert(root.left)
            _invert(root.right)

        return _invert(self.root)

    def traverse(self) -> list[t.Any]:

        values = []

        def _traverse(root: Node | None) -> None:
            if root is None:
                return

            values.append(root.value)
            _traverse(root.left)
            _traverse(root.right)

        _traverse(self.root)
        return values


def main():
    tree = Tree(
        root=Node(4,
            left=Node(2,
                left=Node(1, ),
                right=Node(3, ),
            ),
            right=Node(7,
                left=Node(6, ),
                right=Node(9, ),
            ),
        ),
    )

    tree_2_inverted = Tree(
        root=Node(4,
            left=Node(7,
                left=Node(9, ),
                right=Node(6, ),
            ),
            right=Node(2,
                left=Node(3, ),
                right=Node(1, ),
            ),
        ),
    )

    tree.invert()

    # tree_traversed = tree.traverse()
    # tree_2_inverted_traversed = tree_2_inverted.traverse()

    print(f"Tree: {str(tree)}")
    print(f"Tree (expected): {str(tree_2_inverted)}")

    equals = tree == tree_2_inverted
    assert equals, f"Tree is not properly inverted, {tree} != {tree_2_inverted}"

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
        )
    )

    tree_huge_inverted = Tree(
        root=Node(1,
            left=Node(3,
                left=Node(7,
                    left=Node(15,
                        left=Node(31),
                        right=Node(30),
                    ),
                    right=Node(14,
                        left=Node(29),
                        right=Node(28),
                    ),
                ),
                right=Node(6,
                    left=Node(13,
                        left=Node(27),
                        right=Node(26),
                    ),
                    right=Node(12,
                        left=Node(25),
                        right=Node(24),
                    ),
                ),
            ),
            right=Node(2,
                left=Node(5,
                    left=Node(11,
                        left=Node(23),
                        right=Node(22),
                    ),
                    right=Node(10,
                        left=Node(21),
                        right=Node(20),
                    ),
                ),
                right=Node(4,
                    left=Node(9,
                        left=Node(19),
                        right=Node(18),
                    ),
                    right=Node(8,
                        left=Node(17),
                        right=Node(16),
                    ),
                ),
            ),
        )
    )

    tree_huge.invert()

    print(f"Tree: {str(tree_huge)}")
    print(f"Tree (expected): {str(tree_huge_inverted)}")

    equals = tree_huge == tree_huge_inverted
    assert equals, f"Tree is not properly inverted, {tree_huge} != {tree_huge_inverted}"


if __name__ == '__main__':
    main()
