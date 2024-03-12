# -*- coding: utf-8 -*-
"""
@Author: Federico Bau
@Date: 31/07/2022

MergeSort Implementation using both recursion and loops

< MERGE SORT >
Merge sort is a search Algorithm of type 'Divide and conquer' following this order of logic

* 1) Divide each item in a list/array into one single atomic element possible, basically to is smallest possible
* 2) Compare pairs of elements, sorting its order (desc, asc) and merge it together
* 3) Repeat step 2 until you have one single element again but this time sorted

Complexity (worst): O(n log n).
Space Complexity: O(n)
"""
import time
import random
import threading

class MergeSort:
    """MergeSort class for lists / arrays"""

    PRINT_RESULT = False

    def __init__(self, recursive=True, threads=False):
        self.recursive = threads and False or recursive # if threads is enabled, cannot run in recursive mode
        self.threads = threads
        self.count = 0
        self.start = None
        self.end = None
        self.start_native = None  # Start time of Python native [].sort() method
        self.end_native = None    # End time of Python native [].sort() method

        self.inputs = None
        self.expected = None
        self.order = None

    def __call__(self, inputs: list, expected: list, order='ASC'):
        self.inputs = inputs
        self.expected = expected
        self.order = order

        self.run_recursive()

    def run_recursive(self):
        self.start = time.perf_counter()
        if self.recursive:
            result = self.atomize_and_mergesort_recursive(self.inputs)
        else:
            result = self.atomize_and_mergesort_loop(self.inputs)

        self.end = time.perf_counter()

        self.sort_native()  # Sort list with Python native [].sort() method

        self.check_result(result)

        self.count = 0
        self.start = None
        self.end = None
        self.start_native = None
        self.end_native = None

    # ////////////////////////////
    # ~~~~~~ Recursive ~~~~~~~~~~~
    # ////////////////////////////

    def atomize_and_mergesort_recursive(self, inputs: list):
        """
        Runs merge-sort Algorithm  recursively
        Args:
            inputs (list):

        Returns:
            list : Result of the merge-sort algorithms

        """

        if len(inputs) <= 1:
            return inputs

        left, right = self.divide_in_half(inputs)

        left_merged = self.atomize_and_mergesort_recursive(left)
        right_merged = self.atomize_and_mergesort_recursive(right)

        return self.mergesort_recursive(left_merged, right_merged)

    def mergesort_recursive(self, left: list, right: list) -> list:
        """
        Runs the actual merge-sort algorithm
        Args:
            left (list): left side of the list to be compared
            right (list): right side of the list to be compared

        Returns:
            list: sorted and merged list of left and right inputs
        """
        self.count += 1

        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            left_n = left[i]
            right_n = right[j]

            if left_n < right_n: # Takes from the left list
                result.append(left_n)
                i += 1
                continue

            result.append(right_n) # Takes from the right list
            j += 1

        while i < len(left):  # Consumes any left side entities left-overs
            result.append(left[i])
            i += 1

        while j < len(right):  # Consumes any right side entities left-overs
            result.append(right[j])
            j += 1

        return result

    # ////////////////////////////
    # ~~~~~~~~~ Loop ~~~~~~~~~~~~~
    # ////////////////////////////

    def atomize_and_mergesort_loop(self, inputs: list):
        """
        Runs merge-sort Algorithm  in a loop
        Args:
            inputs (list):

        Returns:
            list : Result of the merge-sort algorithms

        """
        total_values = len(inputs)
        # In order to solve the algorithm it run the same amount of given inputs minus one
        run_times = total_values - 1
        if not run_times:
            return inputs

        atomic_values = [[i] for i in inputs]
        if not self.threads:
            for _ in range(run_times):
                left = atomic_values.pop(0)
                right = atomic_values.pop(0)
                merged = self.mergesort_loop(left, right)
                atomic_values.append(merged)
        else:
            # 1) Create threadings
            threads = []
            for _ in range(run_times):
                new_thread = threading.Thread(target=self.mergesort_loop_thread, args=(atomic_values, ), daemon=True)
                threads.append(new_thread)

            # 2) Start Threadings
            for t in threads:
                t.start()

            # 3) Join threadings
            for t in threads:
                t.join()

        return atomic_values[0]

    def mergesort_loop_thread(self, atomic_values: list) -> list:
        left = atomic_values.pop(0)
        right = atomic_values.pop(0)
        merged = self.mergesort_loop(left, right)
        atomic_values.append(merged)
        return atomic_values



    def mergesort_loop(self, left: list, right: list) -> list:
        """
        Runs the actual merge-sort algorithm
        Args:
            left (list): left side of the list to be compared
            right (list): right side of the list to be compared

        Returns:
            list: sorted and merged list of left and right inputs
        """
        self.count += 1
        result = []
        i = 0
        j = 0
        len_left = len(left)
        len_right = len(right)
        for _ in range(sum([len_left, len_right])):
            if i >= len_left or j >= len_right:
                break
            left_n = left[i]
            right_n = right[j]
            if left_n < right_n:  # Takes from the left list
                result.append(left_n)
                i += 1
                continue

            result.append(right_n)  # Takes from the right list
            j += 1

        # Adds whats left into the result array
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # -----------------------
    #   Helpers
    # -----------------------

    def divide_in_half(self, inputs: list) -> tuple:
        """
        Devide in half inputs
        Args:
            inputs (list): The given inputs

        Returns:
            tuple
        """
        middle = len(inputs) // 2
        return inputs[:middle], inputs[middle:]

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
        """
        Prints to console the MergeSort __call__ result with the native implementation timing
        Args:
            result (list):

        Returns:
            None
        """
        mode = self.recursive and 'RECURSIVE' or 'LOOP'
        if self.threads:
            mode = f'{mode} **thread**'
        total_values = len(self.inputs)
        expected = self.expected
        total_time = self.end - self.start
        total_time_native = self.end_native - self.start_native
        total_time_diff = abs(total_time_native - total_time)
        name = id(self)
        if result != expected:
            if self.PRINT_RESULT:
                print(f"{name} ({mode})  FAILED | Result :: {result} | Expected :: {expected} | Total time: {total_time:.6f} "
                      f"| Native {total_time_native:.6f} | Diff {total_time_diff:.6f} | (vals {total_values} x {self.count} times )")
            else:
                print(f"{name} ({mode}) (x {total_values} vals) FAILED | "
                      f"Total time: {total_time:.6f} | Native {total_time_native:.6f}"
                      f" | Diff {total_time_diff:.6f} | | (vals{total_values} x {self.count} times )")

            return

        if self.PRINT_RESULT:
            print(f"{name} ({mode}) vals) SUCCESS"
                  f" | Total time: {total_time:.6f} | Native {total_time_native:.6f} "
                  f"| Diff {total_time_diff:.6f} |  (vals {total_values} x {self.count} times")
        else:
            print(f"{name} ({mode}) SUCCESS"
                  f" | Total time: {total_time:.6f} | Native {total_time_native:.6f} "
                  f"| Diff {total_time_diff:.6f} | (vals {total_values} x {self.count} times ) ")



def main():
    ms_recursive = MergeSort()
    ms_loop = MergeSort(False)
    ms_loop_threads = MergeSort(False, True)


    print("<<<<<<<<< TEST ONE >>>>>>>>>")
    test_1 = [2, 4, 5, 6, 7, 12, 5]
    ms_recursive(test_1, sorted(test_1))
    ms_loop(test_1, sorted(test_1))
    ms_loop_threads(test_1, sorted(test_1))
    print("----------------------------------------------------- \n")
    print("<<<<<<<<< TEST TWO (50 VALUES) >>>>>>>>>")
    test_2 = [random.randint(0, 500) for _ in range(50)]
    ms_recursive(test_2, sorted(test_2))
    ms_loop(test_2, sorted(test_2))
    ms_loop_threads(test_2, sorted(test_2))
    print("----------------------------------------------------- \n")
    print("<<<<<<<<< TEST THREE (100 VALUES) >>>>>>>>>")
    test_2 = [random.randint(0, 500) for _ in range(100)]
    ms_recursive(test_2, sorted(test_2))
    ms_loop(test_2, sorted(test_2))
    ms_loop_threads(test_2, sorted(test_2))
    print("----------------------------------------------------- \n")
    print("<<<<<<<<< TEST THREE (1000 VALUES) >>>>>>>>>")
    test_2 = [random.randint(0, 500) for _ in range(1000)]
    ms_recursive(test_2, sorted(test_2))
    ms_loop(test_2, sorted(test_2))
    ms_loop_threads(test_2, sorted(test_2))
    print("----------------------------------------------------- \n")
    print("<<<<<<<<< TEST THREE (10000 VALUES) >>>>>>>>>")
    test_2 = [random.randint(0, 500) for _ in range(10000)]
    ms_recursive(test_2, sorted(test_2))
    ms_loop(test_2, sorted(test_2))
    ms_loop_threads(test_2, sorted(test_2))
    print("----------------------------------------------------- \n")
    # print("<<<<<<<<< TEST THREE (100000 VALUES) >>>>>>>>>")
    # test_2 = [random.randint(0, 500) for _ in range(100000)]
    # ms_recursive(test_2, sorted(test_2))
    # ms_loop(test_2, sorted(test_2))
    # ms_loop_threads(test_2, sorted(test_2))
    # print("----------------------------------------------------- \n")
    # print("<<<<<<<<< TEST THREE (1_000_000 VALUES) >>>>>>>>>")
    # test_2 = [random.randint(0, 500) for _ in range(1_000_000)]
    # ms_recursive(test_2, sorted(test_2))
    # ms_loop(test_2, sorted(test_2))
    # ms_loop_threads(test_2, sorted(test_2))
    # print("----------------------------------------------------- \n")
    # print("<<<<<<<<< TEST THREE (10_000_000 VALUES) >>>>>>>>>")
    # test_2 = [random.randint(0, 500) for _ in range(10_000_000)]
    # ms_recursive(test_2, sorted(test_2))
    # ms_loop(test_2, sorted(test_2))
    # ms_loop_threads(test_2, sorted(test_2))
    # print("----------------------------------------------------- \n")
    # print("<<<<<<<<< TEST THREE (100_000_000 VALUES) >>>>>>>>>")
    # test_2 = [random.randint(0, 500) for _ in range(100_000_000)]
    # ms_recursive(test_2, sorted(test_2))
    # ms_loop(test_2, sorted(test_2))
    # ms_loop_threads(test_2, sorted(test_2))
    # print("----------------------------------------------------- \n")


if __name__ == '__main__':
    main()

"""
Results

Ultimatelly with a small quantity of items the loop version runs faster, however as soon as we increase the 
total number to 1000 we can see a noticeably detriment on performance on the loop, being the recursive method 
much much faster. 

That's because the recursive method does not hold in memory the whole list as it splits the array into smaller array 
and solve it separatelly. While the loop, it becomes worst and worst as the items in the arrays grows exponentially



<<<<<<<<< TEST ONE >>>>>>>>>
140594685910320 (RECURSIVE) SUCCESS | Total time: 0.000011 | Native 0.000000 | Diff 0.000011 | (vals 7 x 6 times ) 
140594685910704 (LOOP) SUCCESS | Total time: 0.000010 | Native 0.000000 | Diff 0.000010 | (vals 7 x 6 times ) 
----------------------------------------------------- 

<<<<<<<<< TEST TWO (50 VALUES) >>>>>>>>>
140594685910320 (RECURSIVE) SUCCESS | Total time: 0.000072 | Native 0.000001 | Diff 0.000071 | (vals 50 x 49 times ) 
140594685910704 (LOOP) SUCCESS | Total time: 0.000061 | Native 0.000001 | Diff 0.000060 | (vals 50 x 49 times ) 
----------------------------------------------------- 

<<<<<<<<< TEST THREE (100 VALUES) >>>>>>>>>
140594685910320 (RECURSIVE) SUCCESS | Total time: 0.000153 | Native 0.000003 | Diff 0.000149 | (vals 100 x 99 times ) 
140594685910704 (LOOP) SUCCESS | Total time: 0.000133 | Native 0.000002 | Diff 0.000131 | (vals 100 x 99 times ) 
----------------------------------------------------- 

<<<<<<<<< TEST THREE (1000 VALUES) >>>>>>>>>
140594685910320 (RECURSIVE) SUCCESS | Total time: 0.002021 | Native 0.000064 | Diff 0.001957 | (vals 1000 x 999 times ) 
140594685910704 (LOOP) SUCCESS | Total time: 0.003437 | Native 0.000060 | Diff 0.003377 | (vals 1000 x 999 times ) 
----------------------------------------------------- 

<<<<<<<<< TEST THREE (10000 VALUES) >>>>>>>>>
140594685910320 (RECURSIVE) SUCCESS | Total time: 0.025348 | Native 0.000903 | Diff 0.024445 | (vals 10000 x 9999 times ) 
140594685910704 (LOOP) SUCCESS | Total time: 0.230361 | Native 0.000774 | Diff 0.229586 | (vals 10000 x 9999 times ) 
----------------------------------------------------- 

<<<<<<<<< TEST THREE (100000 VALUES) >>>>>>>>>
140594685910320 (RECURSIVE) SUCCESS | Total time: 0.266994 | Native 0.008446 | Diff 0.258548 | (vals 100000 x 99999 times ) 
140594685910704 (LOOP) SUCCESS | Total time: 20.732353 | Native 0.008190 | Diff 20.724162 | (vals 100000 x 99999 times ) 
----------------------------------------------------- 

<<<<<<<<< TEST THREE (1_000_000 VALUES) >>>>>>>>>
140594685910320 (RECURSIVE) SUCCESS | Total time: 3.255553 | Native 0.092906 | Diff 3.162646 | (vals 1000000 x 999999 times ) 
# unknown. more than 2 minutes
"""