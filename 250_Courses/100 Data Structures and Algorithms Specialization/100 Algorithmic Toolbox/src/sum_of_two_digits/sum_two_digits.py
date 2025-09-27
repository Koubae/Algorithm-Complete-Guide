

def main():
    a, b = map(int, input().split())

    result = algorithm_sum_digits(a, b)
    print(result)
    assert (a + b) == result, f"{a} + {b} == {a + b} != {result}"

def algorithm_sum_digits(a: int, b: int) -> int:
    return a + b 

if __name__ == '__main__':
    main()
