# -*- coding: utf-8 -*-
"""
@Author: Federico Bau
@Date: 31/07/2022

MergeSort Implementation using both recursion and loops

< MERGE SORT >
Merge sort is a search Algorithm of type 'Divide and conquer' following this order of logic

* 1) Divide each item in a list/array into one single atomic element possible, basically to is smallest possible
* 2) Compare pairs of elements, sorting its order (desc, asc) and merge it together
* 3) Repeat step 2 until you have one single element again but this time sorted

Complexity (worst): O(n log n).
Space Complexity: O(n)
"""
import random

def merge_sort(inputs: list) -> list:
    if len(inputs) <= 1:
        return inputs

    middle = len(inputs) // 2
    left = merge_sort(inputs[:middle])
    right = merge_sort(inputs[middle:])

    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        left_n = left[i]
        right_n = right[j]

        if left_n < right_n:
            result.append(left_n)
            i += 1
            continue
        result.append(right_n)
        j += 1
    result += left[i:]
    result += right[j:]

    return result


def main():

    cases = 10
    test_1 = [random.randint(0, 1000) for _ in range(cases)]
    print(f"<<<<<<<<< TEST ONE - CASES {cases}>>>>>>>>>")
    test_1_expected = sorted(test_1)
    result = merge_sort(test_1)
    assert result == test_1_expected
    print("\n----------------------------------------------------- \n")


if __name__ == '__main__':
    main()