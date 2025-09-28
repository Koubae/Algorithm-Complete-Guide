
def quicksort(items: list[int]) -> list[int]:
    if len(items) <= 1:
        return items

    left = []
    right = []
    pivot = items[0]
    for item in items[1:]:
        if item <= pivot:
            left.append(item)
        else:
            right.append(item)
    return quicksort(left) + [pivot] + quicksort(right)


def verify_sort_recursive(items: list[int]) -> bool:
    l = len(items)
    if l <= 1:
        return True

    a = items[0]
    b = items[1]
    return a <= b and verify_sort_recursive(items[1:])


def main():
    numbers = [
        29, 331, 113, 157, 3, 202, 441, 215, 222, 286, 253, 133,
        273, 217, 292, 150, 284, 267, 402, 61, 467, 313, 329, 205,
        383, 347, 406, 8, 61, 259, 279, 85, 497, 435, 163, 364, 409, 405, 97, 107
    ]

    quick_sort = quicksort(numbers)
    check = sorted(numbers)

    assert quick_sort == check, f"Error: merged is not sorted properly:\nmerge_sort: {quick_sort}\ntim_sort: {check}"

    is_sorted = verify_sort_recursive(numbers)
    print(f"numbers verified if are sorted before merge sort: {is_sorted}")

    is_sorted = verify_sort_recursive(quick_sort)
    print(f"numbers verified if are sorted after merge sort: {is_sorted}")



if __name__ == '__main__':
    main()