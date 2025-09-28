/*
@docs: https://en.wikipedia.org/wiki/Binary_search

Semantics are been taken from Wikipedia --> https://en.wikipedia.org/wiki/Binary_search
And to look cooler I keep them but is for sure less clear. But once you get used to it is actually easier
to keep the theory in check

- a: the input array should be sorted (or must be sorted if not yet)
- n: lenght of a
- l: Left pointer/left index 			-- used during binary-search
- r: Right pointer/right index			-- used during binary-search
- m: Position of the middle element		-- used during binary-search
*/
package main

import (
	"errors"
	"fmt"
)

var errTargetNotFound = errors.New("i of t in a not found")

func main() {

	a := [20]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20}
	t := 1

	var err error
	var i int

	i, err = BinarySearch1(a[:], t)
	if err != nil {
		fmt.Printf("Err=%v, T=%v, A=%v \n", err.Error(), t, a)
	} else {
		fmt.Printf("Found Index I of target T in A | I=%v, T=%v, A=%v \n", i, t, a)
	}

}

func BinarySearch1(a []int, t int) (int, error) {
	found := -1
	n := len(a)
	l := 0
	r := n - 1

	var m int
	for l <= r {
		m = l + ((r - l) / 2)
		element := a[m]

		if element == t {
			found = m
			break
		} else if element < t {
			l = m + 1
		} else if element > t {
			r = m - 1
		}

	}

	var err error

	if found == -1 {
		err = errTargetNotFound
	}
	return found, err

}
