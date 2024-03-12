# -*- coding: utf-8 -*-
"""
@Author: Federico Bau
@Date: 01/08/2022


"""

class Node:

    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

    def insert(self, node):
        if not self.value:
            self.value = node
            return

        if node < self.value:
            if not self.left:
                self.left = Node(node)
            else:
                self.left.insert(node)
            return

        if not self.right:
            self.right = Node(node)
        else:
            self.right.insert(node)

    def get_childs(self):
        return [(self.left, self.right)]


    def add_left(self, left):
        self.left = left

    def add_right(self, right):
        self.right = right

    def __str__(self):
        return f"""
 {str(self.value)}
/  \\

"""

    def print_node(self):
        if self.left:
            self.left.print_node()
        print(self),
        if self.right:
            self.right.print_node()

class BinarySearchTree:

    def __init__(self, data):
        self.root = Node(data)
        self.tree = None
        self.target = None
        self.nodes = None

    def __str__(self):
        return f"""{self.root}"""

    def insert(self, node):
        self.root.insert(node)

    def get_nodes(self, mode='default'):


        if mode == 'default':
            nodes = []

            def traverse_simple(root, level):
                if not root:
                    return
                if level >= len(nodes):
                    nodes_level = []
                    nodes.append(nodes_level)

                nodes[level].append(root.value)
                traverse_simple(root.left, level + 1)
                traverse_simple(root.right, level + 1)

            traverse_simple(self.root, 0)
            return nodes
        elif mode == 'mapping':
            nodes = []
            def traverse_mapped(root, level, parent):
                if not root:
                    return
                if level >= len(nodes):
                    nodes_level = []
                    nodes.append(nodes_level)
                parent_key = parent and parent.value or None
                nodes[level].append({root.value: parent_key})
                traverse_mapped(root.left, level + 1, root)
                traverse_mapped(root.right, level + 1, root)

            traverse_mapped(self.root, 0, None)
            return nodes

        elif mode == 'mapping_level':
            nodes = {}
            def traverse_mapped(root, level, parent):
                if not root:
                    return
                if level >= len(nodes):
                    nodes_level = {}
                    nodes[level] = nodes_level
                parent_key = parent and parent.value or None
                if parent_key in nodes[level]:
                    nodes[level][parent_key].append(root.value)
                else:
                    nodes[level][parent_key] = [root.value]
                traverse_mapped(root.left, level + 1, root)
                traverse_mapped(root.right, level + 1, root)

            traverse_mapped(self.root, 0, None)
            return nodes
        else:
            return []





    def print_tree(self):
        if self.root:
            self.root.print_node()
            return
        print('<Empty>')

    def print_tree_all(self):
        if not self.root or not self.root.value:
            print('<Empty>')



if __name__ == '__main__':
    root = BinarySearchTree(10)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(15)
    root.insert(20)
    root.insert(25)
    root.insert(2)
    root.insert(1)
    root.insert(10)
    root.print_tree_all()
    nodes = root.get_nodes()
    print(nodes)

    root2 = BinarySearchTree(10)
    root2.insert(5)
    root2.insert(5)
    root2.insert(2)
    root2.insert(15)
    root2.insert(1)
    root2.insert(2)
    root2.insert(14)
    root2.insert(22)
    root2.insert(13)

    nodes2 = root2.get_nodes('mapping')
    print(nodes2)

    root2 = BinarySearchTree(10)
    root2.insert(5)
    root2.insert(5)
    root2.insert(2)
    root2.insert(15)
    root2.insert(1)
    root2.insert(2)
    root2.insert(14)
    root2.insert(22)
    root2.insert(13)

    nodes2 = root2.get_nodes('mapping_level')
    print(nodes2)
