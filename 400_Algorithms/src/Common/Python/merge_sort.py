# noinspection DuplicatedCode
def merge_sort(array: list) -> list:
    n = len(array)
    if n <= 1:
        return array

    middle = n // 2
    left = merge_sort(array[:middle])       # DFS -- Down all left paths
    right = merge_sort(array[middle:])      # DFS -- Down all right paths

    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        left_value = left[i]
        right_value = right[j]

        if left_value <= right_value:
            i += 1
            result.append(left_value)
        else:
            j += 1
            result.append(right_value)

    while i < len(left):
        value = left[i]
        result.append(value)
        i += 1
    while j < len(right):
        value = right[j]
        result.append(value)
        j += 1
    return result


def main():
    array = [2, 3, 4, 10, 40, 99, 109, 2, 1]

    expected = sorted(array)
    result = merge_sort(expected)
    assert result == expected, f"Expected {expected} got {result}"

    for array in ([], [3, 5, 6], [1, 1,2, 3, 4, 5, 6, 3, 1, 1, 1, ]):
        expected = sorted(array)
        result = merge_sort(expected)
        assert result == expected, f"Expected {expected} got {result}"


if __name__ == '__main__':
    main()
