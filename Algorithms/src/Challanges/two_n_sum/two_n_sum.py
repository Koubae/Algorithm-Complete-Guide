# -*- coding: utf-8 -*-
"""
@Author: Federico Bau
@Date: 31/07/2022

"""

from pprint import pprint

def first_solution(inputs, target):
    visited = {}
    inputs.sort()

    for n in inputs:
        diff = target - n
        if diff in visited:
            return [n, diff]
        visited[n] = True
    return []


def second_solution(inputs, target):

    inputs.sort()
    left_pointer = 0
    right_pointer = -1
    for _ in range(len(inputs)):
        left_v = inputs[left_pointer]
        right_v = inputs[right_pointer]

        total = left_v + right_v
        if total == target:
            return [left_v, right_v]
        elif total < target:
            left_pointer += 1
        else:
            right_pointer -= 1


    return []

if __name__ == '__main__':
    arr = [-7, -5, -3, -1, 0, 1, 3, 5, 7]
    target = -5
    ex = [-5, 0]
    r = first_solution(arr, target)
    assert sorted(r) == sorted(ex)

    r = second_solution(arr, target)
    assert sorted(r) == sorted(ex)