# -*- coding: utf-8 -*-
"""
@Author: Federico Bau
@Date: 31/07/2022

Rules:

1) Loop through inputs values
2) Keep track of the first number of the loop as the minimm values
3) Run nested loop from the current index of main loop to the end.
4) Switch minimum value
5) if minimum value is the same as the current input of main loop continue
6) Else, switch position of the current value with the position of the new smallest values

Complexity (worst): O(n2)
Space Complexity: O(1)
"""
import time
import random


def selection_sort(inputs: list) -> list:
    inputs_count = len(inputs)
    for i in range(inputs_count):
        min_num_index = i
        for j in range(i + 1, inputs_count):
            if inputs[j] < inputs[min_num_index]:
                min_num_index = j

        if min_num_index == i: # if a new value was not found than keep the position as it is and safe some computation
            continue
        # possible variation but slower
        # temp = inputs.pop(min_num_index)
        # current_value = inputs.pop(i)
        # inputs.insert(min_num_index, current_value)
        # inputs.insert(i, temp)

        # switch the position of min value
        temp = inputs[min_num_index]
        inputs[min_num_index] = inputs[i]
        inputs[i] = temp

    return inputs


def main():
    cases = 10
    test_1 = [random.randint(0, 1000) for _ in range(cases)]
    test_1 = [64, 25, 12, 22, 11]
    print(f"<<<<<<<<< TEST ONE - CASES {cases}>>>>>>>>>")
    test_1_expected = sorted(test_1)
    s = time.perf_counter()
    result = selection_sort(test_1)
    e = time.perf_counter()
    print(f'Run {cases} in {(e - s):.6f} result {result}')
    assert test_1_expected == result
    print("\n----------------------------------------------------- \n")

    cases = 100
    test_1 = [random.randint(0, 1000) for _ in range(cases)]
    print(f"<<<<<<<<< TEST ONE - CASES {cases}>>>>>>>>>")
    test_1_expected = sorted(test_1)
    s = time.perf_counter()
    result = selection_sort(test_1)
    e = time.perf_counter()
    print(f'Run {cases} in {(e - s):.6f} ')
    assert test_1_expected == result
    print("\n----------------------------------------------------- \n")

    cases = 1000
    test_1 = [random.randint(0, 1000) for _ in range(cases)]
    print(f"<<<<<<<<< TEST ONE - CASES {cases}>>>>>>>>>")
    test_1_expected = sorted(test_1)
    s = time.perf_counter()
    result = selection_sort(test_1)
    e = time.perf_counter()
    print(f'Run {cases} in {(e - s):.6f} ')
    assert test_1_expected == result
    print("\n----------------------------------------------------- \n")

    cases = 10_000
    test_1 = [random.randint(0, 5) for _ in range(cases)]
    print(f"<<<<<<<<< TEST ONE - CASES {cases}>>>>>>>>>")
    test_1_expected = sorted(test_1)
    s = time.perf_counter()
    result = selection_sort(test_1)
    e = time.perf_counter()
    print(f'Run {cases} in {(e - s):.6f} ')
    assert test_1_expected == result
    print("\n----------------------------------------------------- \n")

    # cases = 100_000
    # test_1 = [random.randint(0, 1000) for _ in range(cases)]
    # print(f"<<<<<<<<< TEST ONE - CASES {cases}>>>>>>>>>")
    # test_1_expected = sorted(test_1)
    # s = time.perf_counter()
    # result = selection_sort(test_1)
    # e = time.perf_counter()
    # print(f'Run {cases} in {(e - s):.6f} ')
    # assert test_1_expected == result
    # print("\n----------------------------------------------------- \n")

    # cases = 1_000_000
    # test_1 = [random.randint(0, 1000) for _ in range(cases)]
    # print(f"<<<<<<<<< TEST ONE - CASES {cases}>>>>>>>>>")
    # test_1_expected = sorted(test_1)
    # s = time.perf_counter()
    # result = selection_sort(test_1)
    # e = time.perf_counter()
    # print(f'Run {cases} in {(e - s):.6f} ')
    # assert test_1_expected == result
    # print("\n----------------------------------------------------- \n")


if __name__ == '__main__':
    main()
