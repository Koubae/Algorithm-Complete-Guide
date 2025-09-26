# -*- coding: utf-8 -*-
"""
@Author: Federico Bau
@Date: 31/07/2022
1) Check that the len of sequence is not more than len of array else RETURN FALSE
2) loop through each number of the sequence
3) If number not in array RETURN FALSE
4) Check that array_found is the same of sequence length, if so break the loop
5) Add the number in the array-found
6) Pop the number found from the array or use a map
7) Check the correct order
"""

from pprint import pprint

def first_solution(array: list, sequence: list) -> bool:
    """

    """
    same_values = []
    for n in array:
        if len(same_values) >= len(sequence):
            break
        if n in sequence:
            same_values.append(n)

    return same_values == sequence


def second_solution(array: list, sequence: list) -> bool:
    """

    """

    in_sequence = list(filter(lambda x : x in sequence, array))[:len(sequence)]
    return in_sequence == sequence

def third_solution(array: list, sequence: list) -> bool:
    sequence_set = set(sequence)
    if len(sequence) == len(sequence_set):
        if not sequence_set.issubset(set(array)):
            return False

    return [n for index, n in enumerate(array) if n in sequence][:len(sequence)] == sequence

def fourth_solution(array: list, sequence: list) -> bool:
    """

    """
    if len(sequence) > len(array):
        return False

    sequence_map = {}

    index_array = 0
    found = []
    while index_array < len(array):
        n = array[index_array]
        index_array += 1
        if n not in sequence:
            continue
        found.append(n)
        if n in sequence_map:
            continue

        total_occurrency_array = array.count(n)
        total_occurrency_sequence = sequence.count(n)
        if total_occurrency_array < total_occurrency_sequence:
            return False
        sequence_map[n] = True

    found = found[:len(sequence)]
    return found == sequence

def fifth_solution(array: list, sequence: list) -> bool:
    """

    """
    if len(sequence) > len(array):
        return False

    sequence_map = {}

    index_array = 0
    found = []

    for index_array in range(len(array)):
        n = array[index_array]
        index_array += 1
        if n not in sequence:
            continue
        found.append(n)
        if n in sequence_map:
            continue

        total_occurrency_array = array.count(n)
        total_occurrency_sequence = sequence.count(n)
        if total_occurrency_array < total_occurrency_sequence:
            return False
        sequence_map[n] = True


    found = found[:len(sequence)]
    return found == sequence

def sixth_solution(array: list, sequence: list) -> bool:
    if len(sequence) > len(array):
        return False

    sequence_index = 0
    array_index = 0

    while sequence_index < len(sequence) and array_index < len(array):

        if sequence_index == len(sequence):
            return True
        value_array = array[array_index]
        value_sequence = sequence[sequence_index]

        if value_array == value_sequence:
            sequence_index += 1 # Move sequence index to the next value
            array_index += 1
            continue
        array_index += 1 # Move the array index forward
    if sequence_index == len(sequence):
        return True
    return False

def seventh_solution(array: list, sequence: list) -> bool:
    if len(sequence) > len(array):
        return False

    index_sequence = 0
    for v in array:
        if index_sequence == len(sequence):
            break
        if sequence[index_sequence] == v:
            index_sequence += 1

    return index_sequence == len(sequence)

if __name__ == '__main__':
    arr =   [1, 1, 1, 1, 1]
    seq =  [1, 1, 1]



    # arr = [1, 1, 1, 1, 1]
    # seq = [1, 1, 1]
    r = first_solution(arr, seq)
    assert r == True
    r = second_solution(arr, seq)
    assert r == True
    r = third_solution(arr, seq)
    assert r == True
    r = third_solution(arr, seq)
    assert r == True

    r = fourth_solution(arr, seq)
    assert r == True

    r = fifth_solution(arr, seq)
    assert r == True

    r = sixth_solution(arr, seq)
    assert r == True

    r = seventh_solution(arr, seq)
    assert r == True