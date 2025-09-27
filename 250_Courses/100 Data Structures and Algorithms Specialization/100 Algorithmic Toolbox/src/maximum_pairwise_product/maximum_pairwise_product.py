
def main():
    _ = input()  # ignore first input 

    numbers = [int(n) for n in input().split()]
    print(max_pairwise_product(numbers))

def max_pairwise_product(numbers: list[int]) -> int:
    n = len(numbers)

    numbers.sort()  
    a, b = numbers[-1], numbers[-2]
    return a * b

if __name__ == '__main__':
    main()

