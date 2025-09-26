"""Binary Tree level order traversal  1"""


class Node:

    def __init__(self, id):
        self.id = id
        self.left = None
        self.right = None

    @staticmethod
    def height(node):
        if node is None:
            return 0
        else:
            left_side = node.height(node.left)
            right_side = node.height(node.right)

            if left_side > right_side:
                return left_side + 1
            else:
                return right_side + 1


# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = root.height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)


# Print nodes at a given level
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.id, end=" ")
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of binary tree is -")
printLevelOrder(root)