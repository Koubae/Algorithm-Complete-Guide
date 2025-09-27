import random
import time
import timeit

def max_pairwise_product_naive(n: int, numbers: list[int]) -> int:
    product = 0
    for i in range(n):
        for j in range(i + 1, n):
            current_product = numbers[i] * numbers[j]
            if current_product > product:
                product = current_product
    return product

def max_pairwise_product_tim_sort(n: int, numbers: list[int]) -> int:
    numbers.sort()  # timSort O(n log n) https://wiki.python.org/moin/TimeComplexity
    a, b = numbers[-1], numbers[-2]
    return a * b

def max_pairwise_product_walker_wrong(n: int, numbers: list[int]) -> int:
    """I don't thik this is correct :)"""
    product = 0
    for i in range(n - 1):
        j = i + 1 # advanced 1

        current_product = numbers[i] * numbers[j]
        if current_product > product:
            product = current_product
    return product

def max_pairwise_product_walker(n: int, numbers: list[int]) -> int:
    """Complexity O(N)

    Iterating in step 2 once only
    This algorithm is really finding the 2 biggest numbers in a list

    """
    a = 0
    b = 0
    for i in range(0, n, 2):
        j = i + 1 # advanced 1

        left = numbers[i]

        if j >= n:
            right = -1  # Odd n the right pointer will overflow, we set it to negative as to "ignore" it
        else:
            right = numbers[j]

        if left < right:  # flip order if left is smaller
            left, right = right, left

        if left > a:  # the left pointer is more "important" since we know this is always true: left > right
            if a > b: # we shouldn't loose current a in case is higher than b then we move it as second bigger n
                b = a
            a = left
        elif left > b:
            b = left

        if right > b:
            b = right
    return a * b

def stress_test_speed():
    random.seed(100)

    n_min_max = (2, 5)
    n_min_max = (2, 10 ** 5)

    nums_min_max = (1, 10 ** 5)

    tests = 1
    i = 0
    while True:
        n = random.randint(*n_min_max)
        numbers = [random.randint(*nums_min_max) for _ in range(n)]
        print(f"Running stress test {i} n={n}")

        naive = timeit.timeit(lambda: max_pairwise_product_naive(n, numbers), number=tests)
        time_sort = timeit.timeit(lambda: max_pairwise_product_tim_sort(n, numbers), number=tests)
        walker = timeit.timeit(lambda: max_pairwise_product_walker(n, numbers), number=tests)

        winner = min(naive, time_sort, walker)
        winners = []
        for v, name in ((naive, "naive"), (time_sort, "time_sort"), (walker, "walker")):
            if v == winner:
                winners.append(name)

        print(f"n={n} naive={naive} time_sort={time_sort} walker={walker} | winners={winners}")
        time.sleep(3)
        i += 1
        if i == 100:
            break

def stress_test_speed_no_naive():
    random.seed(100)

    n_min_max = (2, 5)
    n_min_max = (2, 10 ** 5)

    nums_min_max = (1, 10 ** 5)

    tests = 1
    i = 0
    while True:
        n = random.randint(*n_min_max)
        numbers = [random.randint(*nums_min_max) for _ in range(n)]
        print(f"Running stress test {i} n={n}")

        time_sort = timeit.timeit(lambda: max_pairwise_product_tim_sort(n, numbers), number=tests)
        walker = timeit.timeit(lambda: max_pairwise_product_walker(n, numbers), number=tests)

        winner = min(time_sort, walker)
        losser = max(time_sort, walker)
        winners = []
        for v, name in ((time_sort, "time_sort"), (walker, "walker")):
            if v == winner:
                winners.append(name)

        diff = losser - winner


        print(f"n={n} time_sort={time_sort} walker={walker} | winners={winners} | diff={diff}")
        time.sleep(3)
        i += 1
        if i == 100:
            break


def stress_test_correctness():
    random.seed(100)

    n_min_max = (2, 5)
    n_min_max = (2, 10 ** 5)
    n_min_max = (2, 100)
    nums_min_max = (1, 10 ** 5)
    nums_min_max = (1, 10)

    tests = 100
    i = 0
    max_t = 500_000
    while True:
        n = random.randint(*n_min_max)
        numbers = [random.randint(*nums_min_max) for _ in range(n)]
        print(f"Running stress test {i} n={n}")

        naive = max_pairwise_product_naive(n, numbers.copy())  # naive is out "correct" sample
        time_sort = max_pairwise_product_tim_sort(n, numbers.copy())
        walker = max_pairwise_product_walker(n, numbers.copy())

        is_time_sort_correct = time_sort == naive
        is_walker_correct = walker == naive

        assert is_time_sort_correct, f"time_sort is not correct {time_sort} != {naive} | n={n} numbers={numbers}"
        assert is_walker_correct, f"walker is not correct, {walker} != {naive} |  n={n} numbers={numbers}"

        i += 1
        if i == max_t:
            break

def main(stress: str | None = None) -> None:
    if stress is not None:
        if stress == "SPEED":
            stress_test_speed()
        elif stress == "SPEED_NO_NAIVE":
            stress_test_speed_no_naive()
        elif stress == "CORRECTNESS":
            stress_test_correctness()
        elif stress == "HARD_CODED":
            # result = max_pairwise_product_walker(9, [5, 9, 4, 10, 2, 4, 1, 8, 1])
            result = max_pairwise_product_walker(9, [3, 1, 6, 6, 7, 5, 4, 6, 10])
            print(result)
        else:
            raise ValueError("Invalid stress type")
    else:
        # 5
        # 2 9 3 1 9

        # 20 => 81
        # 8 8 3 7 6 7 9 2 9 2 2 8 5 1 4 6 4 5 4 3

        # 9 => 90
        # 5 9 4 10 2 4 1 8 1
        # [5, 9, 4, 10, 2, 4, 1, 8, 1]

        # 9 => 70
        # 3 1 6 6 7 5 4 6 10
        # [3, 1, 6, 6, 7, 5, 4, 6, 10]

        n = int(input() ) # ignore first input
        numbers = [int(n) for n in input().split()]
        # result = max_pairwise_product_naive(n, numbers)
        result = max_pairwise_product_walker(n, numbers)
        print(result)

if __name__ == '__main__':
    import os
    # print(os.system("dir"))
    STRESS_TYPE = "SPEED"
    STRESS_TYPE = None
    STRESS_TYPE = "HARD_CODED"
    STRESS_TYPE = "CORRECTNESS"
    STRESS_TYPE = "SPEED_NO_NAIVE"
    main(STRESS_TYPE)


