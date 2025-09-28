
def merge_sort(items: list[int]) -> list[int]:
    """
    - Time complexity: O(n log n)
    - Space complexity: O(n)

    - Divide: Find the midpoint and divide the items into two sublists
    - Conquer: Recursively sort the two sublists created in the previous step
    - Combine: Merge the sorted sublists created in a previous step
    """
    l = len(items)
    if l <= 1:
        return items

    # split in haf
    mid = l // 2
    left_partition = items[:mid]
    right_right_partition = items[mid:]

    left = merge_sort(left_partition)
    right = merge_sort(right_right_partition)

    # merge
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        left_item = left[i]
        right_item = right[j]

        if left_item < right_item:
            merged.append(left_item)
            i += 1  # increase a left pointer
        else:
            merged.append(right_item)
            j += 1 # increase a right pointer

    # compute remaining left elements
    while i < len(left):
        merged.append(left[i])
        i += 1

    # compute remaining right elements
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

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

    merged = merge_sort(numbers)
    check = sorted(numbers)

    assert merged == check, f"Error: merged is not sorted properly:\nmerge_sort: {merged}\ntim_sort: {check}"

    is_sorted = verify_sort_recursive(numbers)
    print(f"numbers verified if are sorted before merge sort: {is_sorted}")

    is_sorted = verify_sort_recursive(merged)
    print(f"numbers verified if are sorted after merge sort: {is_sorted}")

if __name__ == '__main__':
    main()