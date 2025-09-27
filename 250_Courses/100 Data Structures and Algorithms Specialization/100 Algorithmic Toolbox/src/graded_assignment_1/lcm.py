def lcm_original(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False

def gcd(a, b):
    if b == 0:
        return a

    a_prime = a % b
    return gcd(b, a_prime)


def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

if __name__ == '__main__':
    # 761457 614573 => 467970912861
    a, b = map(int, input().split())
    print(lcm(a, b))

