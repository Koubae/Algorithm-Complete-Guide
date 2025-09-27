def fibonacci_last_digit_original(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def fibonacci_last_digit(n: int) -> int:
    if n <= 1:
        return n

    # Pisano period for mod 10 is 60
    n %= 60
    if n == 0:
        n = 60

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current


if __name__ == '__main__':
    testing = False
    if not testing:
        n = int(input())
        print(fibonacci_last_digit(n))
    else:
        # tests = [(3, 2), (139, 1), ]
        # tests = [(3, 2), (139, 1), (91_239, 6),]
        # tests = [(999999, 6),]
        tests = [(240, 0),]

        for n, expected in tests:
            result = fibonacci_last_digit(n)
            print(result)
            assert result == expected, f"Expected {expected} got {result}"
            # break
