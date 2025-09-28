def binary_search(n: list, target: int) -> int:
    """
    Time - Complexity O(log n)
    Space - Complexity O(1)

    """
    index = -1
    l = len(n)
    left = 0
    right = l - 1
    while left <= right:

        middle = (left + right) // 2
        current = n[middle]
        if current == target:
            index = middle
            break
        elif current < target: # advance left pointer
            left = middle + 1
        elif current > target:
            right = middle -1  # recede a right pointer
    return index

def binary_search_recursive_1(n: list, target: int) -> int:
    """
    Time - Complexity O(log n)
    Space - Complexity O(log n)

    This should be worsted in Space complexity than the iterative version
    Each time we call the recursion function, we create a new stack frame and create a new sub-list.
    and the recursion caller keeps the previous list in the memory-stack till the end of the recursion.
    """

    def recursion(_n: list, _target: int) -> bool:
        l = len(_n)
        if l == 0:
            return False

        middle = l // 2
        current = _n[middle]
        if current == _target:
            return True
        if current < _target:
            return recursion(_n[middle+1:], _target)
        else:
            return recursion(_n[:middle], _target)

    result = recursion(n, target)
    return result


def binary_search_recursive_2(n: list, target: int) -> int:
    """
    Time - Complexity O(log n)
    Space - Complexity O(1)
    """

    l = len(n)

    def recursion(left: int, right: int) -> int:
        if left > right:
            return -1

        middle = (left + right) // 2
        current = n[middle]
        if current == target:
            return middle
        elif current < target:
            return recursion(middle + 1, right)
        else:
            return recursion(left, middle - 1)

    index = recursion(0, l - 1)
    return index


def verify(n: list, target: int, expected: int) -> None:
    index = binary_search(n, target)
    assert index == expected, f"Error: {index} != {expected}"

def verify_recursive_1(n: list, target: int, expected: bool) -> None:
    found = binary_search_recursive_1(n, target)
    assert found == expected, f"Error: target {target} should have been '{expected}' but got '{found}'"

def verify_recursive_2(n: list, target: int, expected: int) -> None:
    index = binary_search_recursive_2(n, target)
    assert index == expected, f"Error: {index} != {expected}"

def main():
    # numbers = [i for i in range(1, 21)]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    verify(numbers, 1, 0)
    verify(numbers, 10, 9)
    verify(numbers, 12, 11)
    verify(numbers, 20, 19)
    verify(numbers, 50, -1)

    verify_recursive_1(numbers, 1, True)
    verify_recursive_1(numbers, 10, True)
    verify_recursive_1(numbers, 12, True)
    verify_recursive_1(numbers, 20, True)
    verify_recursive_1(numbers, 50, False)

    verify_recursive_2(numbers, 1, 0)
    verify_recursive_2(numbers, 10, 9)
    verify_recursive_2(numbers, 12, 11)
    verify_recursive_2(numbers, 20, 19)
    verify_recursive_2(numbers, 50, -1)
    verify_recursive_2(numbers, 500, -1)
    verify_recursive_2([i for i in range(1, 500)], 500, -1)
    verify_recursive_2([i for i in range(1, 501)], 500, 499)



if __name__ == '__main__':
    main()