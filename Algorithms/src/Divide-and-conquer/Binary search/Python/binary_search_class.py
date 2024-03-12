# -*- coding: utf-8 -*-
"""
@Author: Federico Bau
@Date: 30/07/2022

Simple Representation of a Binary search both recursively or with a loop

"""


class BinarySearch:

    def __init__(self, inputs: set, recursive=False):
        self.inputs = self.sort_inputs(inputs)
        self.recursive = recursive

    def __call__(self, run_name, target, expected) -> int:
        self.run_name = run_name
        self.target = target
        self.expected = expected

        if self.recursive:
            return self.search_recursive()
        return self.search()

    def search(self) -> int:
        elements = self.inputs
        target = self.target
        total_elements = len(elements)

        left = 0
        right = total_elements - 1
        found = -1
        for loop in range(total_elements):

            middle = self.get_middle(left, right)
            current_value = self.get_current_value(elements, middle)
            if current_value == -1:
                found = -1
                break

            if current_value == target: # check if we found the element
                found = middle
                break

            # Now we determine wether we go to the left side or to the right side
            which_half = self.which_way_to_go(current_value, target)
            if which_half == "RIGHT":  # if value is less then target then we move to right side
                left = middle + 1
            elif which_half == "LEFT":  # if value is more than target then we move to the left side
                right = middle -1


        # Calcualte result and return
        self.test_results(found)
        return found




    def search_recursive(self) -> int:

        elements = self.inputs
        target = self.target

        def search(left, right) -> int:
            if not left <= right:
                return -1

            middle = self.get_middle(left, right)
            current_value = self.get_current_value(elements, middle)
            if current_value == -1:
                return current_value

            if current_value == target:  # check if we found the element
                return middle

            which_half = self.which_way_to_go(current_value, target)
            if which_half == "RIGHT":  # if value is less then target then we move to right side
                return search(middle + 1, right)
            elif which_half == "LEFT":  # if value is more than target then we move to the left side
                return search(left, middle - 1)

            return -1

        result = search(0, len(elements) - 1)
        self.test_results(result)
        return result

    def test_results(self, result: int) -> None:
        run_name = self.run_name
        target = self.target
        expected = self.expected

        if result == -1:  # then is not found
            print(f'Test run {run_name} Not found!!!: <Element {target} ==>  NOT_FOUND > ')
            return

        if expected != result:
            print(
                f'Test run {run_name} Failed!!!: <Element {target} ==> NOT_FOUND Got -> {result} Expected {expected} > ')
            return
        print(f'Test run {run_name} Success!!!: <Element {target} ==> {result} > ')

    # ----------
    #   Helpers
    # ----------

    def get_current_value(self, elements: list, middle: int) -> int:
        try:
            return elements[middle]
        except IndexError as err:
            self.test_results(-1)

        return -1

    def get_middle(self, left: int, right: int) -> int:
        return (left + right) // 2

    def which_way_to_go(self, current_value: int, target: int) -> str:
        if current_value < target:  # if value is less then target then we move to right side
            return "RIGHT"
        elif current_value > target:  # if value is more than target then we move to the left side
            return "LEFT"
        return ""

    @staticmethod
    def sort_inputs(inputs: set) -> list:
        inputs = list(inputs)
        inputs.sort()
        return inputs


if __name__ == '__main__':
    sorted_fruits = [
        'apple',
        'banana',
        'orange',
        'plum',
        'thing',
        'other',
        'thing',
        'thing',
        'other'
    ]

    # Test 1
    test_1_inputs = {10, 20, 30, 50, 60, 80, 110, 130, 140, 170}
    test_1_target = 110
    test_1_expected = 6
    result_1 = (BinarySearch(test_1_inputs, True))("Run 1 (Recursive)", test_1_target, test_1_expected)

    # Test 2
    test_2_inputs = {10, 20, 30, 40, 60, 110, 120, 130, 170}
    test_2_target = 175
    test_2_expected = -1
    result_2 = (BinarySearch(test_2_inputs, True))("Run 2 (Recursive)", test_2_target, test_2_expected)

    # Test 3
    test_3_inputs = {10, 20, 30, 50, 60, 80, 110, 130, 140, 170}
    test_3_target = 110
    test_3_expected = 6
    result_3 = (BinarySearch(test_3_inputs, False))("Run 3 (Loop)", test_3_target, test_3_expected)

    # Test 4
    test_4_inputs = {10, 20, 30, 40, 60, 110, 120, 130, 170}
    test_4_target = 175
    test_4_expected = -1
    result_4 = (BinarySearch(test_4_inputs, False))("Run 4 (Loop)", test_4_target, test_4_expected)
