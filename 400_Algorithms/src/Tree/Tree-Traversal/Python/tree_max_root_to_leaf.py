# noinspection DuplicatedCode
"""
Max Root to Leaf -- Depth-First Search (DFS)

Given a binary tree, find the maximum value at the root to leaf path.

Example:
               1
         2         3
      7    5      8  4
    8  9  3  1  15 3

The max path is 1 -> 3 -> 8 -> 15 = 27
               1
                  3
                8
              15
"""
import typing as t
from collections import deque
from copy import deepcopy
from dataclasses import dataclass, field, replace as dataclass_replace


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
class Path:
    weight: int
    path: deque[str]
    nodes: deque[Node]

    @classmethod
    def new(cls) -> t.Self:
        return Path(weight=0, path=deque(), nodes=deque())

    def deep_copy(self) -> t.Self:
        new = Path(weight=self.weight, path=deepcopy(self.path), nodes=deepcopy(self.nodes))
        return new


@dataclass
class Tree:
    root: Node | None = field(default=None)

    def dfs_max_root_to_leaf_count(self) -> int:
        """We only care to count the max path value and not return the actual path.
        Preorder Root --> left --> right
        """
        if self.root is None:
            return 0

        def _recursive(node: Node | None) -> int:
            if node is None:
                return 0

            # 1) we need to check if we have a leaf node
            is_leaf = node.left is None and node.right is None
            if is_leaf:
                return node.value

            left_count = _recursive(node.left)
            right_count = _recursive(node.right)

            return node.value + max(left_count, right_count)

        return _recursive(self.root)

    def dfs_max_root_to_leaf_path(self) -> Path | None:
        """
        Preorder Root --> left --> right
        """
        if self.root is None:
            return Path.new()

        def _recursive(node: Node | None) -> Path | None:
            if node is None:
                return None

            is_leaf = node.left is None and node.right is None
            if is_leaf:
                path = Path.new()
                path.weight += node.value
                path.nodes.appendleft(node)
                return path

            left = _recursive(node.left)
            right = _recursive(node.right)

            if not left and not right:
                return None

            if left and not right:
                longest = left
                direction = "left"
            elif right and not left:
                longest = right
                direction = "right"
            else:
                longest = left if left.weight >= right.weight else right
                direction = "left" if left.weight >= right.weight else "right"

            longest.weight += node.value
            longest.nodes.appendleft(node)
            longest.path.appendleft(direction)
            return longest

        return _recursive(self.root)


def main():
    tree = Tree(
        root=Node(1,
            left=Node(2,
                left=Node(7,
                    left=Node(8, ),
                    right=Node(9),
                ),
                right=Node(5,
                    left=Node(3),
                    right=Node(1),
                ),
            ),
            right=Node(3,
                left=Node(8,
                    left=Node(15),
                    right=Node(3),
                ),
                right=Node(4, ),
            ),
        ),
    )

    expected = 27
    max_count = tree.dfs_max_root_to_leaf_count()
    assert max_count == expected, f"Expected {expected}, got {max_count}"

    path = tree.dfs_max_root_to_leaf_path()
    print(f"Path: {path}")

    expected_path = ["right", "left", "left"]
    assert path.weight == expected, f"Path weight {expected}, got {path.weight}"
    assert path.path == deque(expected_path), f"Path path {expected_path}, got {path.path}"

    # Now follow the path and assert that brings to expected nodes
    root = path.nodes[0]
    for node, path in zip(list(path.nodes)[1:], path.path):
        node_expected = getattr(root, path, None)
        print(f"Path direction from {root} {path} => {node_expected}")

        assert node == node_expected, f"Node {node} expected {node_expected}, got {node}"
        assert node.value == node_expected.value, f"Node value {node.value} expected {node_expected.value}, got {node.value}"

        root = node



    tree = Tree(
        root=Node(1,
            left=Node(2,
                left=Node(7,
                    left=Node(8, ),
                    right=Node(9),
                ),
                right=Node(5,
                    left=Node(3),
                    right=Node(1),
                ),
            ),
        ),
    )

    expected = 19
    max_count = tree.dfs_max_root_to_leaf_count()
    assert max_count == expected, f"Expected {expected}, got {max_count}"
    path = tree.dfs_max_root_to_leaf_path()
    print(f"Path: {path}")

    expected_path = ['left', 'left', 'right']
    assert path.weight == expected, f"Path weight {expected}, got {path.weight}"
    assert path.path == deque(expected_path), f"Path path {expected_path}, got {path.path}"

    # Now follow the path and assert that brings to expected nodes
    root = path.nodes[0]
    for node, path in zip(list(path.nodes)[1:], path.path):
        node_expected = getattr(root, path, None)
        print(f"Path direction from {root} {path} => {node_expected}")

        assert node == node_expected, f"Node {node} expected {node_expected}, got {node}"
        assert node.value == node_expected.value, f"Node value {node.value} expected {node_expected.value}, got {node.value}"

        root = node

if __name__ == '__main__':
    main()
