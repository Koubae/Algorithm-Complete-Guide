import math

def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m



def fib(n):
    """Binet’s Formula"""
    phi = (1 + math.sqrt(5)) / 2
    return round((phi**n - (-1/phi)**n) / math.sqrt(5))

def pisano_period(m: int) -> int:
    # Returns π(m). Worst-case O(m^2).
    prev, curr = 0, 1
    for i in range(m * m + 1):  # safe upper bound
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            return i + 1

def fib_mod_fast_doubling(n: int, m: int) -> int:
    # Returns F_n mod m in O(log n)
    def fd(k: int) -> tuple[int, int]:
        if k == 0:
            return 0, 1
        a, b = fd(k >> 1)
        c = (a * ((b << 1) - a)) % m        # F(2m)
        d = (a * a + b * b) % m             # F(2m+1)
        return (d, (c + d) % m) if (k & 1) else (c, d)
    return fd(n)[0]

def fib_mod_using_pisano(n: int, m: int) -> int:
    p = pisano_period(m)
    return fib_mod_fast_doubling(n % p, m)



if __name__ == '__main__':
    # 2816213588 239 => 151
    n, m = map(int, input().split())
    print(fib_mod_using_pisano(n, m))
