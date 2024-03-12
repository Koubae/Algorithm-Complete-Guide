# -*- coding: utf-8 -*-
"""
@Author: Federico Bau
@Date: 01/08/2022


"""


def first_solution(array: list, targetSum: int) -> list:
    """ Find Triples in given array that sum up to target sum
    Rules
    * Numbers inside triples must be asc ordered
    * Triples MUST be ordered ASC
    * if not found, return empty array
    """

    result = []

    array.sort()
    for index_i, first_number in enumerate(array):
        for second_number_index in range(index_i + 1, len(array)):
            second_number = array[second_number_index]

            third_number_up = second_number_index + 1
            for third_number_index in range(third_number_up, len(array)):
                third_number = array[third_number_index]

                sum_tripplet = first_number + second_number + third_number
                if sum_tripplet == targetSum:
                    tripplet = [first_number, second_number, third_number]
                    tripplet.sort()
                    result.append(tripplet)

    result.sort()
    return result


def second_solution(array: list, targetSum: int) -> list:
    """ Find Triples in given array that sum up to target sum
    Rules
    * Numbers inside triples must be asc ordered
    * Triples MUST be ordered ASC
    * if not found, return empty array
    """

    result = []

    array.sort()
    total_len = len(array)
    for index_i, first_number in enumerate(array):

        pointer_left = index_i + 1
        pointer_right = total_len - 1
        while pointer_left <= total_len-1 and pointer_right <= total_len-1:
            if pointer_left == pointer_right:  # reach the middle point
                break

            second_number = array[pointer_left]
            third_number = array[pointer_right]

            current_sum = first_number + second_number + third_number
            if current_sum == targetSum:
                tripplet = [first_number, second_number, third_number]
                tripplet.sort()
                result.append(tripplet)

            if current_sum < targetSum:
                pointer_left += 1
            else:
                pointer_right -= 1

    result.sort()
    return result

if __name__ == '__main__':
    # array = [1, 2, 3]
    # targetSum = 6

    array = [12, 3, 1, 2, -6, 5, -8, 6]
    targetSum = 0
    output = [
        [-8, 2, 6],
        [-8, 3, 5],
        [-6, 1, 5]
    ]
    result = first_solution(array, targetSum)
    print(f'result {result}')
    assert result == output

    result = second_solution(array, targetSum)
    print(f'result {result}')
    assert result == output
