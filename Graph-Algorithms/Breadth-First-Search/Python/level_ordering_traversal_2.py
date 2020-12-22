"""Binary Tree level order traversal  2"""


class Node:
    def __init__(self, id):
        self.id = id
        self.left = None
        self.right = None

    def __repr__(self):
        return f'Node: {self.id}'


def build_bin_tree(root):

    if not root:
        return

    queue = []
    queue.append(root)
    binary_tree = []
    while queue:

        node = queue.pop(0)
        binary_tree.append(node)
        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)
    return binary_tree

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
result = build_bin_tree(root)
print(result)