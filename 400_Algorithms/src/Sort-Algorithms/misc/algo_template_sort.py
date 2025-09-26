# -*- coding: utf-8 -*-
"""
@Author: Federico Bau
@Date: 31/07/2022

Rules:

Complexity (worst):
Space Complexity:
"""
import time
import random

class AlgoSort:

    def __init__(self):
        self.count = 0
        self.start = None
        self.end = None
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
        self.start = time.perf_counter()
        result = self.algorithm()
        self.end = time.perf_counter()

        self.sort_native()  # Sort list with Python native [].sort() method

        self.check_result(result)

        self.reset_algo()

    def algorithm(self) -> list:
        inputs = self.inputs
        result = []

        return result


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
        inputs_copy = self.inputs.copy() # make a copy so that the original input is not modified
        self.start_native = time.perf_counter()
        inputs_copy.sort()
        self.end_native = time.perf_counter()

    def check_result(self, result: list) -> None:

        total_values = len(self.inputs)
        expected = self.expected
        total_time = self.end - self.start
        total_time_native = self.end_native - self.start_native
        total_time_diff = abs(total_time_native - total_time)
        name = id(self)

        assert expected == result
        print(f"""Runner {name} SUCCESS
        * Total time: {total_time:.6f}
        * Native {total_time_native:.6f}
        * Diff {total_time_diff:.6f}
        * Volume: {total_values} items  x {self.count} times
        """)

    def reset_algo(self):
        self.count = 0
        self.start = None
        self.end = None
        self.start_native = None
        self.end_native = None

def main():
    qs = AlgoSort()


    cases = 10
    test_1 = [random.randint(0, 1000) for _ in range(cases)]
    print(f"<<<<<<<<< TEST ONE - CASES {cases}>>>>>>>>>")
    test_1_expected = sorted(test_1)
    qs(test_1, test_1_expected)
    print("\n----------------------------------------------------- \n")

if __name__ == '__main__':
    main()
