"""
Fibonacci using the Pisano period
https://en.wikipedia.org/wiki/Pisano_period

For modulus 10, the cycle length is 60.

F(60) % 10 = F(0) % 10
F(61) % 10 = F(1) % 10

F(10^18)
10^18 mod 60 = r
"""

def fibonacci_pisano_period(n: int) -> int:
    if n <= 1:
        return n

    r = n % 60
    if r == 0:
        r = 60

    a, b = 0, 1
    for _ in range(r - 1):
        a, b = b, (a + b) % 10
    return b

def main():
    i = 100

    fibonacci_sequence = [fibonacci_pisano_period(n) for n in range(i)]
    print(fibonacci_sequence)


if __name__ == '__main__':
    main()