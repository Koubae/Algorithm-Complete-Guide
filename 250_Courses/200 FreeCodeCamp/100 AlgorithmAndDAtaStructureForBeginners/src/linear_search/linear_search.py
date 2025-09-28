def linear_search(n: list, target: int) -> int:
    """Complexity O(n)"""
    index = -1

    for i in range(len(n)):
        current = n[i]
        if current == target:
            index = i
            break

    return index

def verify(n: list, target: int, expected: int) -> None:
    index = linear_search(n, target)
    assert index == expected, f"Error: {index} != {expected}"

def main():
    # numbers = [i for i in range(1, 21)]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    verify(numbers, 1, 0)
    verify(numbers, 10, 9)
    verify(numbers, 12, 11)
    verify(numbers, 20, 19)


if __name__ == '__main__':
    main()