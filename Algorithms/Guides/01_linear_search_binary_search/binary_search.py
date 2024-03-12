def binary_search(values, target):
    """
    Complexity : O(log n)

    Args:
        values ():
        target ():

    Returns:

    """
    values.sort() # Make sure are sorted otherwise this binary search will not work
    first = 0
    last = len(values) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if values[midpoint] == target:
            return midpoint

        if values[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return


def binary_search_recursive(values: list, target: int) -> bool:
    """
        Complexity : O(log n)

        Args:
            values (list):
            target (int):

        Returns:

        """
    if not len(values):
        return False

    midpoint = (len(values)) // 2

    if values[midpoint] == target:
        return True

    if values[midpoint] < target:
        return binary_search_recursive(values[midpoint+1:], target)
    else:
        return binary_search_recursive(values[:midpoint], target)


if __name__ == '__main__':
    # Binary Search
    nums = list(range(1, 11))  # 1 --> 10 nums
    test_1 = 12
    print(f"Test for n {test_1} --> {binary_search(nums, test_1)}")

    test_1 = 6
    print(f"Test for n {test_1} --> {binary_search(nums, test_1)}")

    test_1 = 7
    print(f"Test for n {test_1} --> {binary_search(nums, test_1)}")

    # Binary Search Recursive
    nums = list(range(1, 11))  # 1 --> 10 nums
    test_1 = 12
    print(f"Test for n {test_1} --> {binary_search_recursive(nums, test_1)}")

    test_1 = 6
    print(f"Test for n {test_1} --> {binary_search_recursive(nums, test_1)}")

    test_1 = 7
    print(f"Test for n {test_1} --> {binary_search_recursive(nums, test_1)}")