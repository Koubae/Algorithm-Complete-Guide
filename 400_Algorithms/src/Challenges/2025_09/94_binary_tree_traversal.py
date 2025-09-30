
from typing import Optional, List
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        if root is None:
            return traversal

        def _traverse(node: Optional[TreeNode]) -> None:
            if node is None:
                return

            _traverse(node.left)
            traversal.append(node.val)
            _traverse(node.right)

        _traverse(root)
        return traversal
