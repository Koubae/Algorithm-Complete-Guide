# noinspection DuplicatedCode
def quick_sort(array: list) -> list:
    n = len(array)
    if n <= 1:
        return array

    left = []
    right = []
    pivot = array[0]

    for i in range(1, n):
        value = array[i]

        if value < pivot:
            left.append(value)
        else:
            right.append(value)

    return quick_sort(left) + [pivot] + quick_sort(right)


def main():
    array = [2, 3, 4, 10, 40, 99, 109, 2, 1]

    expected = sorted(array)
    result = quick_sort(expected)
    assert result == expected, f"Expected {expected} got {result}"

    for array in ([], [3, 5, 6], [1, 1, 2, 3, 4, 5, 6, 3, 1, 1, 1, ]):
        expected = sorted(array)
        result = quick_sort(expected)
        assert result == expected, f"Expected {expected} got {result}"

if __name__ == '__main__':
    main()
