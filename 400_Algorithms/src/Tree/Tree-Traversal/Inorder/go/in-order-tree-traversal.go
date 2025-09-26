/*
@credit: (problem) https://leetcode.com/problems/binary-tree-inorder-traversal/description/
@credit: (solution) https://en.wikipedia.org/wiki/Tree_traversal#In-order_implementation
*/

package main

import (
	"fmt"
	"reflect"
)

type Node struct {
	Val   int
	Left  *Node
	Right *Node
}

func main() {

	root := &Node{Val: 1}

	root.Left = &Node{Val: 2}
	root.Left.Left = &Node{Val: 4}
	root.Left.Right = &Node{Val: 5}
	root.Left.Right.Left = &Node{Val: 6}
	root.Left.Right.Right = &Node{Val: 7}

	root.Right = &Node{Val: 3}
	root.Right.Right = &Node{Val: 8}
	root.Right.Right.Left = &Node{Val: 9}

	Print(root, "", false)

	result := inorderTraversal(root)

	expected := []int{4, 2, 6, 5, 7, 1, 3, 9, 8}

	fmt.Println("\nInorder traversal:")
	fmt.Println(result)
	fmt.Println(reflect.DeepEqual(result, expected))

}

// @credit: (solution) https://en.wikipedia.org/wiki/Tree_traversal#In-order_implementation
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

func Print(root *Node, prefix string, isLeft bool) {
	if root == nil {
		return
	}

	// Right child first
	if root.Right != nil {
		newPrefix := prefix
		if isLeft {
			newPrefix += "│   "
		} else {
			newPrefix += "    "
		}
		Print(root.Right, newPrefix, false)
	}

	// Current node
	fmt.Print(prefix)
	if isLeft {
		fmt.Print("└── ")
	} else {
		fmt.Print("┌── ")
	}
	fmt.Println(root.Val)

	// Left child
	if root.Left != nil {
		newPrefix := prefix
		if isLeft {
			newPrefix += "    "
		} else {
			newPrefix += "│   "
		}
		Print(root.Left, newPrefix, true)
	}
}
