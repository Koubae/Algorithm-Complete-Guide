package main

import "fmt"

type Node struct {
	Val   int
	Left  *Node
	Right *Node
}

type Tree struct {
	Root *Node
}

// ChatGPT 5 credit
func (t *Tree) Print(root *Node, prefix string, isLeft bool) {
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
		t.Print(root.Right, newPrefix, false)
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
		t.Print(root.Left, newPrefix, true)
	}
}

func (t *Tree) Invert(root *Node) *Node {
	if root == nil {
		return nil
	}

	root.Left, root.Right = root.Right, root.Left
	t.Invert(root.Left)
	t.Invert(root.Right)
	return root
}

func main() {
	var tree Tree

	root := &Node{Val: 0}
	tree.Root = root

	root.Left = &Node{Val: 1}
	root.Right = &Node{Val: 2}

	root.Left.Left = &Node{Val: 3}
	root.Left.Right = &Node{Val: 4}

	root.Right.Left = &Node{Val: 5}
	root.Right.Right = &Node{Val: 6}

	root.Left.Left.Left = &Node{Val: 7}
	root.Left.Left.Right = &Node{Val: 8}
	root.Left.Right.Left = &Node{Val: 9}
	root.Left.Right.Right = &Node{Val: 10}

	root.Right.Left.Left = &Node{Val: 11}
	root.Right.Left.Right = &Node{Val: 12}
	root.Right.Right.Left = &Node{Val: 13}
	root.Right.Right.Right = &Node{Val: 14}

	// tree.Print(tree.Root, 0)
	fmt.Println("Original tree:")
	tree.Print(root, "", false)

	tree.Invert(root)
	fmt.Println("Inverted tree:")
	tree.Print(root, "", false)

}
