package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const AskInput = false

func main() {

	sequence := getSequenceInput()
	BubbleSort(sequence) // Since we are working with a slice which contains a pointer we don't need an explicit pointer
	for _, v := range sequence {
		fmt.Printf("%d ", v)
	}

}

func getSequenceInput() []int {
	defaultInput := [...]int{20, 30, 999, 33, 44, 10, 40, 50, -1, -2, 3, 4, 500, 1, 3, -2, 0, 1, 300, 200, 8, 10}
	if !AskInput {
		return defaultInput[:]
	}
	fmt.Printf(
		"Enter sequence of numbers, separated by space or just press enter to use a default sequence: %v\n",
		defaultInput,
	)

	reader := bufio.NewReader(os.Stdin)
	data, err := reader.ReadString('\n')
	if err != nil {
		fmt.Printf("Error while reading user input, errror: %v\n", err)
		os.Exit(1)
	}

	nums := strings.Fields(data)
	sequence := make([]int, len(nums))
	for i, num := range nums {
		value, err := strconv.Atoi(num)
		if err != nil {
			fmt.Printf("Wrong sequence of number, num '%s' is not a valid number, errror: %v\n", num, err)
			os.Exit(1)
		}

		sequence[i] = value
	}

	if len(sequence) == 0 {
		// If user inputs nothing we use a default sequence, just to be faster during development
		return defaultInput[:]
	}

	return sequence
}

func BubbleSort(sequence []int) {
	l := len(sequence)

	for i := range l {
		swapped := false

		for j := range l - i - 1 {

			left := sequence[j]
			right := sequence[j+1]
			if left > right {
				sequence[j] = right
				sequence[j+1] = left
				// Swap(sequence, j)
				swapped = true
			}
		}

		if !swapped {
			break
		}

	}
}

func Swap(sequence []int, j int) {
	left := sequence[j]
	right := sequence[j+1]

	sequence[j] = right
	sequence[j+1] = left

}

// bubbleSort sorts an integer slice using bubble sort algorithm
func bubbleSortChatGPT_Generated(arr []int) {
	n := len(arr)
	for i := 0; i < n-1; i++ {
		swapped := false
		for j := 0; j < n-i-1; j++ {
			if arr[j] > arr[j+1] {
				// swap arr[j] and arr[j+1]
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = true
			}
		}
		// if no elements were swapped, the array is already sorted
		if !swapped {
			break
		}
	}
}
