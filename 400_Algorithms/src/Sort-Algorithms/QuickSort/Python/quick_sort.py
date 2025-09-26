# -*- coding: utf-8 -*-
"""
@Author: Federico Bau
@Date: 31/07/2022

Rules:

1) Take 'pivot' from list
2) Put smaller values of pivot into list 'lesser' and greater in 'greater'
3) Call function recursively by merging the result like lesser + [pivot] + greater

Complexity (worst): Quadratic O(n²).
Space Complexity: O(n)
"""
import random


def quicksort(inputs: list) -> list:
    """
    Runs a quicksort algorithm
    Args:
        inputs (list):

    Returns:
        list: sorted values
    """
    if len(inputs) <= 1:
        return inputs

    lesser = []
    greater = []
    pivot = inputs[0]

    for v in inputs[1:]:
        if v <= pivot:
            lesser.append(v)
            continue
        greater.append(v)

    return quicksort(lesser) + [pivot] + quicksort(greater)

def quicksort_test():
    cases = 10
    test_1 = [random.randint(0, 1000) for _ in range(cases)]
    test_1_expected = sorted(test_1)
    result = quicksort(test_1)
    print(result)
    assert test_1_expected == result

if __name__ == '__main__':
    quicksort_test()
