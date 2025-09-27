def max_pairwise_product_walker(n: int, numbers: list[int]) -> int:
    """Complexity O(N)

    Iterating in step 2 once only
    This algorithm is really finding the 2 biggest numbers in a list

    """
    a = 0
    b = 0
    for i in range(0, n, 2):
        j = i + 1 # advanced 1

        left = numbers[i]

        if j >= n:
            right = -1  # Odd n the right pointer will overflow, we set it to negative as to "ignore" it
        else:
            right = numbers[j]

        if left < right:  # flip order if left is smaller
            left, right = right, left

        if left > a:  # the left pointer is more "important" since we know this is always true: left > right
            if a > b: # we shouldn't loose current a in case is higher than b then we move it as second bigger n
                b = a
            a = left
        elif left > b:
            b = left

        if right > b:
            b = right
    return a * b

def main() -> None:
    n = int(input())
    numbers = [int(n) for n in input().split()]
    result = max_pairwise_product_walker(n, numbers)
    print(result)


if __name__ == '__main__':
    main()


