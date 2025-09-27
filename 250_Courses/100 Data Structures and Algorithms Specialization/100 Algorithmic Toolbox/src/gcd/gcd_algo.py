
def gcd_naive(a: int, b: int) -> int:
    best = 0
    for d in range(1, a + b):
        if a % d == 0 and b % d == 0:
            best = d
    return best

def gcd_naive2(a: int, b: int) -> int:
    best = 0
    for d in range(1, min(a, b ) + 1) :
        if a % d == 0 and b % d == 0:
            if d > best:
                best = d
    return best

def gcd_euclidian_algorithm(a: int, b: int) -> int:
    """Euclidean algorithmEuclidean algorithm https://en.wikipedia.org/wiki/Euclidean_algorithm"""
    if b == 0:
        return a

    a_prime = a % b
    return gcd_euclidian_algorithm(b, a_prime)


def main():
    result = gcd_naive(12, 15)
    print(result)
    assert result == 3, f"expected 3 got {result}"

    result = gcd_naive2(12, 15)
    print(result)
    assert result == 3, f"expected 3 got {result}"

    result = gcd_euclidian_algorithm(357, 234)
    print(result)
    assert result == 3, f"expected 3 got {result}"
    result = gcd_euclidian_algorithm(3_918_848, 1_653_264)
    print(result)
    assert result == 61_232, f"Expected 61232 got {result}"

if __name__ == '__main__':
    main()