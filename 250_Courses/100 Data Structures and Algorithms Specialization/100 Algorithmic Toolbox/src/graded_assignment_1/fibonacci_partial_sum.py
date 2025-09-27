# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10


# def fibonacci_mod(n: int, m: int) -> int:
#     """Return F(n) mod m using Pisano period."""
#     if n <= 1:
#         return n
#     n %= 60  # Pisano period for mod 10 is 60
#     prev, curr = 0, 1
#     for _ in range(n - 1):
#         prev, curr = curr, (prev + curr) % m
#     return curr
#
# def fibonacci_partial_sum(from_, to):
#     # sum F(from_..to) = F(to+2) - F(from_+1)
#     last = fibonacci_mod(to + 2, 10)
#     first = fibonacci_mod(from_ + 1, 10)
#     return (last - first) % 10



def fibonacci_partial_sum(from_, to) -> int:
    # Pisano period for mod 10 is 60
    from_ %= 60
    to %= 60

    if to < from_:  # wrap around the period
        to += 60

    _sum = 0
    prev, curr = 0, 1
    for i in range(1, to + 1):
        if i >= from_:
            _sum = (_sum + curr) % 10
        prev, curr = curr, (prev + curr) % 10

    return _sum

if __name__ == '__main__':
    # input = sys.stdin.read();
    from_, to = map(int, input().split())
    # from_, to = (1, 100000000)  # -> 5
    # from_, to = (1, 2)  # -> 2
    # from_, to = (1, 3)  # -> 4
    # from_, to = (1234, 12345)  # -> 8
    print(fibonacci_partial_sum(from_, to))
