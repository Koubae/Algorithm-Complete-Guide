# -*- coding: utf-8 -*-
"""
@Author: Federico Bau
@Date: 31/07/2022
r
"""
import math
from pprint import pprint

def first_solution(array: list) -> list:
    a = [i**2 for i in array]
    a.sort()
    return a

def second_solution(array: list) -> list:
    return sorted([math.pow(i, 2) for i in array])

def third_solution(array: list) -> list:

    # Power in place the items without creating a new array
    for index, i in enumerate(array):
        array[index] = i ** 2

    # Create a quick sort
    def quick_sort(inputs: list) -> list:
        if len(inputs) <= 1:
            return inputs
        pivot = inputs[0]
        lesser = []
        greater = []
        for n in inputs[1:]:
            if n < pivot:
                lesser.append(n)
                continue
            greater.append(n)

        return quick_sort(lesser) + [pivot] + quick_sort(greater)

    return quick_sort(array)

if __name__ == '__main__':
    arr = [1, 2, 3, 5, 6, 8, 9]
    expected = [1, 4, 9, 25, 36, 64, 81]
    result = first_solution(arr)
    assert result == expected

    result = second_solution(arr)
    assert result == expected

    result = third_solution(arr)
    assert result == expected
