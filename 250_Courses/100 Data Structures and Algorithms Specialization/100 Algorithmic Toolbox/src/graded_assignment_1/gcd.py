def gcd_original(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd(a, b):
    if b == 0:
        return a

    a_prime = a % b
    return gcd(b, a_prime)


if __name__ == "__main__":
    # 28851538 1183019 => 17657
    a, b = map(int, input().split())
    print(gcd(a, b))
