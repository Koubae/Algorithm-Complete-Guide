def fibonacci_sum_original(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

def fibonacci_sum(n: int) -> int:
    if n <= 1:
        return n

    # Pisano period for modulo 10 is 60
    n = (n + 2) % 60

    prev, curr = 0, 1
    for _ in range(n - 1):
        prev, curr = curr, (prev + curr) % 10

    # F(n+2) - 1, take care of wrap-around
    return (curr - 1) % 10

if __name__ == '__main__':
    n = int(input())
    # n = 613455
    print(fibonacci_sum(n))
