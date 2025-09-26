# -*- coding: utf-8 -*-
"""
@Author: Federico Bau
@Date: 31/07/2022

The insertion sort is somewhat similar to the selection sort but moves backward each time when a smaller
value is found instead of swapping the values as it moves forward

Rules:

1) Iterate/Loop through inputs values starting at index 1
2) Store the current value at index as 'key'
3) Create a nested iteration from the current index backward
4) Values of the nested iteration will compare with the current 'key' value
5) If the current key is smaller than nested current value then move the key behind
6) Repeat until the main iteration ends

Complexity (worst): O(n2)
Space Complexity: O(1)
"""
import time
import random


def insertion_sort(inputs: list) -> list:

    # Iterate/Loop through inputs values
    for current_index in range(1, len(inputs)):
        current_value = inputs[current_index]
        previous_index = current_index - 1

        while previous_index >= 0 and current_value < inputs[previous_index]:
            inputs[previous_index + 1] = inputs[previous_index]
            previous_index -= 1

        if previous_index + 1 == current_index: # avoid useless computation, means that the current value stays where it is
            continue
        inputs[previous_index + 1] = current_value

    return inputs


def main():
    cases = 10
    test_1 = [random.randint(0, 1000) for _ in range(cases)]
    print(f"<<<<<<<<< TEST ONE - CASES {cases}>>>>>>>>>")
    test_1_expected = sorted(test_1)
    s = time.perf_counter()
    result = insertion_sort(test_1)
    e = time.perf_counter()
    print(f'Run {cases} in {(e - s):.6f} result {result}, expected {test_1_expected}')
    assert test_1_expected == result
    print("\n----------------------------------------------------- \n")

    cases = 100
    test_1 = [random.randint(0, 1000) for _ in range(cases)]
    print(f"<<<<<<<<< TEST ONE - CASES {cases}>>>>>>>>>")
    test_1_expected = sorted(test_1)
    s = time.perf_counter()
    result = insertion_sort(test_1)
    e = time.perf_counter()
    print(f'Run {cases} in {(e - s):.6f}')
    assert test_1_expected == result
    print("\n----------------------------------------------------- \n")

    cases = 1000
    test_1 = [random.randint(0, 1000) for _ in range(cases)]
    print(f"<<<<<<<<< TEST ONE - CASES {cases}>>>>>>>>>")
    test_1_expected = sorted(test_1)
    s = time.perf_counter()
    result = insertion_sort(test_1)
    e = time.perf_counter()
    print(f'Run {cases} in {(e - s):.6f}')
    assert test_1_expected == result
    print("\n----------------------------------------------------- \n")

    cases = 10_000
    test_1 = [random.randint(0, 1000) for _ in range(cases)]
    print(f"<<<<<<<<< TEST ONE - CASES {cases}>>>>>>>>>")
    test_1_expected = sorted(test_1)
    s = time.perf_counter()
    result = insertion_sort(test_1)
    e = time.perf_counter()
    print(f'Run {cases} in {(e - s):.6f}')
    assert test_1_expected == result
    print("\n----------------------------------------------------- \n")

    cases = 100_000
    test_1 = [random.randint(0, 1000) for _ in range(cases)]
    print(f"<<<<<<<<< TEST ONE - CASES {cases}>>>>>>>>>")
    test_1_expected = sorted(test_1)
    s = time.perf_counter()
    result = insertion_sort(test_1)
    e = time.perf_counter()
    print(f'Run {cases} in {(e - s):.6f}')
    assert test_1_expected == result
    print("\n----------------------------------------------------- \n")


if __name__ == '__main__':
    main()
