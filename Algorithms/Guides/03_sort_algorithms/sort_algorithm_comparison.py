# -*- coding: utf-8 -*-
"""
@Author: Federico Bau
@Date: 31/07/2022

Include the following algorithms

* Native python [].sort() method
* Insertion Sort
* Selection Sort
* Merge Sort
* Quick Sort

"""
import time
import random


class SortingAlgorithms:

    def __init__(self):
        # Insertion-Sort Algo
        self.count_insertion = 0
        self.start_insertion = None
        self.end_insertion = None
        # Selection-Sort Algo
        self.count_selection = 0
        self.start_selection = None
        self.end_selection = None
        # Merge-Sort Algo
        self.count_merge = 0
        self.start_merge = None
        self.end_merge = None
        # Quick-Sort Algo
        self.count_quick = 0
        self.start_quick = None
        self.end_quick = None
        # Sort-native (Tim-sort) Algo
        self.start_native = None  # Start time of Python native [].sort() method
        self.end_native = None  # End time of Python native [].sort() method

        self.inputs = None
        self.expected = None
        self.order = None

    def __call__(self, inputs: list, expected: list, order='ASC'):
        self.inputs = inputs
        self.expected = expected
        self.order = order

        self.run()

    def run(self):
        # Create 4 copy of the input so that each algorithm will have is onw copy
        # yes, at larger value this may implode you machine but well...
        input_insertion = self.inputs.copy()
        input_selection = self.inputs.copy()
        input_merge = self.inputs.copy()
        input_quick = self.inputs.copy()

        # Insertion-Sort Algo
        self.start_insertion = time.perf_counter()
        result_insertion = self.insertion_sort(input_insertion)
        self.end_insertion = time.perf_counter()

        # Selection-Sort Algo
        self.start_selection = time.perf_counter()
        result_selection = self.selection_sort(input_selection)
        self.end_selection = time.perf_counter()

        # Merge-Sort Algo
        self.start_merge = time.perf_counter()
        result_merge = self.merge_sort(input_merge)
        self.end_merge = time.perf_counter()

        # Quick-Sort Algo
        self.start_quick = time.perf_counter()
        result_quick = self.quick_sort(input_quick)
        self.end_quick = time.perf_counter()

        # Sort-native (Tim-sort) Algo
        self.sort_native()  # Sort list with Python native [].sort() method

        self.check_result([
            result_insertion,
            result_selection,
            result_merge,
            result_quick
        ])
        self.reset_algo()

    def insertion_sort(self, inputs: list) -> list:

        for current_index in range(1, len(inputs)):
            self.count_insertion += 1
            current_value = inputs[current_index]
            previous_index = current_index - 1

            # go backward and compare previous values
            while previous_index >= 0 and current_value < inputs[previous_index]:
                self.count_insertion += 1
                inputs[previous_index + 1] = inputs[previous_index]
                previous_index -= 1

            # check if the index is the same
            if previous_index + 1 == current_index:
                continue
            inputs[previous_index + 1] = current_value

        return inputs

    def selection_sort(self, inputs: list) -> list:

        len_inputs = len(inputs)
        for current_index in range(len_inputs - 1):
            self.count_selection += 1
            smallest_n_index = current_index

            for next_index in range(current_index + 1, len_inputs):
                self.count_selection += 1
                if inputs[next_index] < inputs[smallest_n_index]:
                    smallest_n_index = next_index

            if smallest_n_index == current_index:
                continue

            temp = inputs[smallest_n_index]
            inputs[smallest_n_index] = inputs[current_index]
            inputs[current_index] = temp

        return inputs

    def merge_sort(self, inputs: list) -> list:
        if len(inputs) <= 1:
            return inputs

        self.count_merge += 1
        middle = len(inputs) // 2
        left = self.merge_sort(inputs[:middle])
        right = self.merge_sort(inputs[middle:])

        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            self.count_merge += 1
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

    def quick_sort(self, inputs: list) -> list:
        self.count_quick += 1
        if len(inputs) <= 1:
            return inputs

        pivot = inputs[0]
        lessers = []
        greaters = []
        for v in inputs[1:]:
            self.count_quick += 1
            if v <= pivot:
                lessers.append(v)
                continue
            greaters.append(v)

        return self.quick_sort(lessers) + [pivot] + self.quick_sort(greaters)

    # ////////////////////////////
    # ~~~~~~ Recursive ~~~~~~~~~~~
    # ////////////////////////////

    # -----------------------
    #   Helpers
    # -----------------------

    def sort_native(self) -> None:
        """
        Sorts the inputs list using native method [].sort() and records its timing
        Returns:
            None
        """
        inputs_copy = self.inputs.copy()  # make a copy so that the original input is not modified
        self.start_native = time.perf_counter()
        inputs_copy.sort()
        self.end_native = time.perf_counter()

    def check_result(self, results: list) -> None:
        total_values = len(self.inputs)
        expected = self.expected

        total_time_insertion = self.end_insertion - self.start_insertion
        total_time_selection = self.end_selection - self.start_selection
        total_time_merge = self.end_merge - self.start_merge
        total_time_quick = self.end_quick - self.start_quick
        total_time_native = self.end_native - self.start_native
        min_time = min([
            total_time_insertion,
            total_time_selection,
            total_time_merge,
            total_time_quick,
            total_time_native
        ])

        winner = total_time_insertion == min_time and 'Insertion' or \
                 total_time_selection == min_time and 'Selection' or \
                 total_time_merge == min_time and 'Merge-Sort' or \
                 total_time_quick == min_time and 'Quick-Sort' or \
                 total_time_native == min_time and 'Sort-native (Tim-sort)' or \
                 'Unknown'

        min_time_no_native = min([
            total_time_insertion,
            total_time_selection,
            total_time_merge,
            total_time_quick,
        ])

        winner_no_native = total_time_insertion == min_time_no_native and 'Insertion' or \
                           total_time_selection == min_time_no_native and 'Selection' or \
                           total_time_merge == min_time_no_native and 'Merge-Sort' or \
                           total_time_quick == min_time_no_native and 'Quick-Sort' or \
                           'Unknown'

        name = id(self)

        [result_insertion, result_selection, result_merge, result_quick] = results

        assert expected == result_insertion
        assert expected == result_selection
        assert expected == result_merge
        assert expected == result_quick

        print(f"""Runner {name} SUCCESS
        -------- < TIMINGS > ----------- 
        * Insertion: {total_time_insertion:.6f}
        * Selection: {total_time_selection:.6f}
        * Merge-Sort: {total_time_merge:.6f}
        * Quick-Sort: {total_time_quick:.6f}
        * Sort-native (Tim-sort) {total_time_native:.6f}
        * Winner: {winner}
        * Winner (Native excluded): {winner_no_native}

        -------- < VOLUMES > ----------- 
        * Total Values: {total_values}
        * Insertion: {self.count_insertion} times
        * Selection: {self.count_selection} times
        * Merge-Sort: {self.count_merge} times
        * Quick-Sort: {self.count_quick} times
        """)

    def reset_algo(self):
        # Insertion-Sort Algo
        self.count_insertion = 0
        self.start_insertion = None
        self.end_insertion = None
        # Selection-Sort Algo
        self.count_selection = 0
        self.start_selection = None
        self.end_selection = None
        # Merge-Sort Algo
        self.count_merge = 0
        self.start_merge = None
        self.end_merge = None
        # Quick-Sort Algo
        self.count_quick = 0
        self.start_quick = None
        self.end_quick = None
        # Sort-native (Tim-sort) Algo
        self.start_native = None  # Start time of Python native [].sort() method
        self.end_native = None  # End time of Python native [].sort() method


def main():
    qs = SortingAlgorithms()

    cases = 10
    test_1 = [random.randint(0, 1000) for _ in range(cases)]
    print(f"<<<<<<<<< TEST ONE - CASES {cases}>>>>>>>>>")
    test_1_expected = sorted(test_1)
    qs(test_1, test_1_expected)
    print("\n----------------------------------------------------- \n")

    cases = 100
    test_1 = [random.randint(0, 1000) for _ in range(cases)]
    print(f"<<<<<<<<< TEST ONE - CASES {cases}>>>>>>>>>")
    test_1_expected = sorted(test_1)
    qs(test_1, test_1_expected)
    print("\n----------------------------------------------------- \n")

    cases = 1000
    test_1 = [random.randint(0, 1000) for _ in range(cases)]
    print(f"<<<<<<<<< TEST ONE - CASES {cases}>>>>>>>>>")
    test_1_expected = sorted(test_1)
    qs(test_1, test_1_expected)
    print("\n----------------------------------------------------- \n")

    cases = 10_000
    test_1 = [random.randint(0, 1000) for _ in range(cases)]
    print(f"<<<<<<<<< TEST ONE - CASES {cases}>>>>>>>>>")
    test_1_expected = sorted(test_1)
    qs(test_1, test_1_expected)
    print("\n----------------------------------------------------- \n")


if __name__ == '__main__':
    main()

"""
<<<<<<<<< TEST ONE - CASES 10>>>>>>>>>
Runner 139705109252896 SUCCESS
        -------- < TIMINGS > ----------- 
        * Insertion: 0.000007
        * Selection: 0.000008
        * Merge-Sort: 0.000015
        * Quick-Sort: 0.000010
        * Sort-native (Tim-sort) 0.000000
        * Winner: Sort-native (Tim-sort)
        * Winner (Native excluded): Insertion

        -------- < VOLUMES > ----------- 
        * Total Values: 10
        * Insertion: 33 times
        * Selection: 54 times
        * Merge-Sort: 33 times
        * Quick-Sort: 41 times


----------------------------------------------------- 

<<<<<<<<< TEST ONE - CASES 100>>>>>>>>>
Runner 139705109252896 SUCCESS
        -------- < TIMINGS > ----------- 
        * Insertion: 0.000310
        * Selection: 0.000458
        * Merge-Sort: 0.000178
        * Quick-Sort: 0.000206
        * Sort-native (Tim-sort) 0.000005
        * Winner: Sort-native (Tim-sort)
        * Winner (Native excluded): Merge-Sort

        -------- < VOLUMES > ----------- 
        * Total Values: 100
        * Insertion: 2443 times
        * Selection: 5049 times
        * Merge-Sort: 638 times
        * Quick-Sort: 863 times


----------------------------------------------------- 

<<<<<<<<< TEST ONE - CASES 1000>>>>>>>>>
Runner 139705109252896 SUCCESS
        -------- < TIMINGS > ----------- 
        * Insertion: 0.030768
        * Selection: 0.040371
        * Merge-Sort: 0.002123
        * Quick-Sort: 0.001376
        * Sort-native (Tim-sort) 0.000062
        * Winner: Sort-native (Tim-sort)
        * Winner (Native excluded): Quick-Sort

        -------- < VOLUMES > ----------- 
        * Total Values: 1000
        * Insertion: 248142 times
        * Selection: 500499 times
        * Merge-Sort: 9725 times
        * Quick-Sort: 11595 times


----------------------------------------------------- 

<<<<<<<<< TEST ONE - CASES 10000>>>>>>>>>
Runner 139705109252896 SUCCESS
        -------- < TIMINGS > ----------- 
        * Insertion: 3.162029
        * Selection: 4.127694
        * Merge-Sort: 0.026144
        * Quick-Sort: 0.020551
        * Sort-native (Tim-sort) 0.000776
        * Winner: Sort-native (Tim-sort)
        * Winner (Native excluded): Quick-Sort

        -------- < VOLUMES > ----------- 
        * Total Values: 10000
        * Insertion: 24874190 times
        * Selection: 50004999 times
        * Merge-Sort: 130413 times
        * Quick-Sort: 187675 times


----------------------------------------------------- 


Process finished with exit code 0


"""