def linear_search(array: list[int], target: int) -> int:
    n = len(array)
    i = 0
    found = -1
    for i in range(n):
        current = array[i]
        if current == target:
            found = i
            break
        i += 1
    return found

def main():
    array = [2, 3, 4, 10, 40, 99, 109, 2, 1]
    array.sort()

    target = 109
    expected = array.index(target)

    found = linear_search(array, target)

    assert found == expected, f"Target {target} should be {expected} got: {found} in array => {array}"

    for i in array:
        expected = array.index(i)
        found = linear_search(array, i)
        assert found == expected, f"Target {i} should be {expected} got: {found} in array => {array}"

    target = 9999
    expected = -1
    found = linear_search(array, target)
    assert found == expected, f"Target {target} should be {expected} got: {found} in array => {array}"


if __name__ == '__main__':
    main()
