from functools import cache
import timeit

def fib_naive(n: int) -> int:
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

@cache
def fib_naive_cache(n: int) -> int:
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

def fib_list(n : int) -> int:
    _nums = [
        0, 1
    ]
    for i in range(2, n+1):
        _nums.append(_nums[i-1] + _nums[i-2])
    return _nums[-1]

def fib_last_two(n: int) -> int:
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    results = [fib_naive(i) for i in range(11)]
    print(results)

    # print(fib_naive(20))
    print(fib_naive_cache(35))
    print(fib_list(35))
    print(fib_last_two(35))
    repetitions = 10
    n = 30

    naive = timeit.timeit(lambda: fib_naive(n), number=repetitions)
    using_cache = timeit.timeit(lambda: fib_naive_cache(n), number=repetitions)
    using_list = timeit.timeit(lambda: fib_list(n), number=repetitions)
    using_fib_last_two = timeit.timeit(lambda: fib_last_two(n), number=repetitions)

    cache_diff = naive - using_cache
    fib_list_diff = naive - using_list
    fib_list_diff_vs_cache = using_cache - using_list

    using_fib_last_two_diff = naive - using_fib_last_two
    using_fib_last_two_diff_vs_cache = using_cache - using_fib_last_two
    using_fib_last_two_diff_vs_list = using_list - using_fib_last_two


    print(f"n={n} | rep={repetitions} ")
    print(f"Naive: {naive} | Cache: {using_cache} | naive-cache: {cache_diff}")
    print(f"using_list: {using_list} |  naive-list: {fib_list_diff}, cache - list: {fib_list_diff_vs_cache}")
    print(f"using_fib_last_two: {using_fib_last_two} | naive-fib_last_two: {using_fib_last_two_diff}, cache - fib_last_two: {using_fib_last_two_diff_vs_cache}, list - fib_last_two: {using_fib_last_two_diff_vs_list}")

if __name__ == '__main__':
    main()