# noinspection DuplicatedCode
def binary_search(array: list[int], target: int) -> int:
    n = len(array)
    left = 0
    right = n - 1
    found = -1

    while left <= right:
        middle = (left + right) // 2

        current = array[middle]
        if current == target:
            found = middle
            break

        if current < target:
            left = middle + 1
        else:
            right = middle - 1

    return found

def main():
    array = [2, 3, 4, 10, 40, 99, 109, 2, 1]
    array.sort()

    target = 109
    expected = array.index(target)

    found = binary_search(array, target)

    assert found == expected, f"Target {target} should be {expected} got: {found} in array => {array}"

    for i in array:
        expected = array.index(i)
        found = binary_search(array, i)
        assert found == expected, f"Target {i} should be {expected} got: {found} in array => {array}"

    target = 9999
    expected = -1
    found = binary_search(array, target)
    assert found == expected, f"Target {target} should be {expected} got: {found} in array => {array}"


if __name__ == '__main__':
    main()
