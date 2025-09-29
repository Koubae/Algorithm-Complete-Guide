# noinspection DuplicatedCode
"""

https://leetcode.com/problems/binary-tree-inorder-traversal/description/
https://leetcode.com/problems/invert-binary-tree/description/
"""
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


def main():
    #### Binary Tree
    tree_1 = Tree(
        root=Node(1,
            left=Node(2,
                left=Node(4,
                    right=Node(8),
                ),
                right=Node(5),
            ),

            right=Node(3,
                left=Node(6,
                    left=Node(9),
                    right=Node(10),
                ),
                right=Node(7),
            ),
        ),
    )

    tree_2 = Tree(
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

    tree_2_inversed = Tree(
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

    #### Binary Search Trees (BST)

    bst_1 = Tree(
        root=Node(8,
            left=Node(3,
                left=Node(1),
                right=Node(6,
                    left=Node(4),
                    right=Node(7),
                ),
            ),
            right=Node(10,
                right=Node(14,
                    left=Node(13),
                ),
            ),
        ),
    )
    bst_2 = Tree(root=Node(10))
    bst_3 = Tree(root=Node(10, left=Node(5, left=Node(2, left=Node(1)))))


if __name__ == '__main__':
    main()
