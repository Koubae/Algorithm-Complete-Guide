Graphs -- DFS -- Inorder
=========================

* [Inorder](https://en.wikipedia.org/wiki/Tree_traversal#In-order_implementation)
* [Inorder (LeetCode Challange)](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)
* [Inorder geeksforgeeks](https://www.geeksforgeeks.org/dsa/inorder-traversal-of-binary-tree/)


Implementation (go) see [in-order-tree-traversal.go](in-order-tree-traversal.go)

```go
func inorderTraversal(root *Node) []int {
	var algo func(node *Node)

	result := make([]int, 0)
	algo = func(node *Node) {
		if node == nil {
			return
		}

		algo(node.Left)
		result = append(result, node.Val)
		algo(node.Right)

	}
	algo(root)
	return result
}
```