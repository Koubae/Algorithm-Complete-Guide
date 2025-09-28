import time

def binary_search(a: list[int], t: int) -> int:
    i = -1
    n = len(a)
    l = 0
    r = n - 1

    while l <= r:
        m = l + ((r - l) // 2)

        element = a[m]
        if element == t:
            i = m
            break
        if element < t:
             l = m + 1
        elif element > t:
            r = m - 1
    if i == -1:
        raise BinarySearchNotFound(f"t {t} not found in A")

    return i


class BinarySearchNotFound(Exception):
    pass

def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for t in (8, 1, 4, 19, 20, 14):
        i = binary_search(a, t)
        print(f"Found at index {i} t={t} \ta={a}")
        time.sleep(.3)

if __name__ == '__main__':
    main()
