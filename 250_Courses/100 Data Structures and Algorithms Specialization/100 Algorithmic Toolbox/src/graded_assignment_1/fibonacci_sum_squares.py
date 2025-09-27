def fibonacci_sum_squares_original(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fibonacci_sum_squares(n: int) -> int:
    if n <= 1:
        return n
    elif n == 2:
        return 2

    # Pisano period for mod 10 is 60
    n %= 60
    if n == 0:
        n = 60

    previous, current, sum = 0, 1, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
        sum += current * current

    return sum % 10

if __name__ == '__main__':
    n = int(input())
    # n = 78134 # => 78
    # n = 2 # => 2
    # n = 3 # => 6
    print(fibonacci_sum_squares(n))
