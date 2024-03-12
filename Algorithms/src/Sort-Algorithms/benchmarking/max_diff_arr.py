import itertools
from collections import deque
import random
from time import perf_counter
import copy
# =================== < BRUTE FORCE > =================== #
def brute_force(l):
    result = 0

    for i in itertools.permutations(l):
        if diff_sum(i) > result:
            result = diff_sum(i)

    return result


# =================== < ORIGINAL SOLUTION > =================== #
def maximum_difference_sort(data: list, *, start_with_max=True):
    queue = deque()
    indices = [0, -1] if start_with_max else [-1, 0]
    queue.append(data.pop(indices[1]))
    while True:
        try:
            queue.append(data.pop(indices[0]))
            queue.appendleft(data.pop(indices[0]))

            queue.append(data.pop(indices[1]))
            queue.appendleft(data.pop(indices[1]))
        except IndexError:
            break
    return list(queue)


def combined_difference(seq):
    s = 0
    for i in range(1, len(seq)):
        s += abs(seq[i] - seq[i-1])
    return s

# --------------------------------------------------------------


# =================== < FIRST VARIATION > =================== #
def sumDiffs(R): return sum(abs(a - b) for a, b in zip(R, R[1:]))


def maxDiffs(A):
    if len(A) <= 2: return sumDiffs(A), A
    S = sorted(A)
    first = [S.pop(len(S) // 2)]
    half = len(S) // 2
    lower = S[:half]
    upper = S[-half:]
    last = S[half:-half]

    def interlace(L, R):
        return [n for ab in zip(L, R) for n in ab]

    patterns = []
    for L, R in [(lower, upper), (upper, lower)]:
        for ld, rd in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            patterns.append(first + interlace(L[::ld], R[::rd]) + last)
    return max((sumDiffs(p), p) for p in patterns)

# --------------------------------------------------------------

# =================== < SECOND VARIATION > =================== #
def big_little_sort(l):
    s = sorted(l)
    result = []
    result.append(s.pop())

    while len(s):
        if s:
            result.insert(len(result), s.pop(0))
        if s:
            result.insert(0, s.pop(0))
        if s:
            result.insert(len(result), s.pop(-1))
        if s:
            result.insert(0, s.pop(-1))

    return result

def diff_sum(l):
    result = 0
    for i in range(len(l[:-1])):
        result += abs(l[i] - l[i+1])
    return result

# --------------------------------------------------------------

# =================== < MY SOLUTION > =================== #
def algorithm(input_list):

    max_difference = 0
    # --------------- List Sorting & Setting Up Max And Min Pip
    input_list.sort()
    half = len(input_list)//2
    max_pipe = input_list[half:]
    min_pipe = input_list[:half]
    # --------------- Loop Utils
    total_comparison = len(input_list) - 2
    counter = 1
    offset = 0

    # --------------- Algorithm
    for n in range(half//2):
        if counter == total_comparison:  # The Algorithm can have only a certain and precise amount of calculations
            break
        comparison = 0
        for N in max_pipe[-counter::-1]:

            max_difference += N - min_pipe[offset*2]
            max_difference += N - min_pipe[offset*2 + 1]
            comparison += 1
            if comparison == 2:  # NOTE: Only 2 Comparison for each couple (Max, Min) num
                break
        counter += 2
        offset += 1

    max_difference += max_pipe[0] - min_pipe[-1]  # Last calculation left over
    return max_difference


# -------- Create Cases
n = 40  # items in list
m = 10000  # repetitions
lo = 0
hi = 100
cases = [random.sample(range(lo, hi), n) for i in range(m)]
cases_original = copy.deepcopy(cases)
cases_first = copy.deepcopy(cases)
cases_second = copy.deepcopy(cases)
cases_my = copy.deepcopy(cases)

# -------- Original
test_start_1 = perf_counter()
for i in cases_original:
    i.sort()
    combined_difference(maximum_difference_sort(i, start_with_max=True))
test_stop_1 = perf_counter()
final_org = test_stop_1 - test_start_1
# -------- First Solution
test_start_2 = perf_counter()
for j in cases_first:
    maxDiffs(j)
test_stop_2 = perf_counter()
final_first = test_stop_2 - test_start_2


# -------- Second Solution
test_start_3 = perf_counter()
for k in cases_second:
    diff_sum(big_little_sort(k))
test_stop_3 = perf_counter()
final_second = test_stop_3 - test_start_3


# -------- MY SOLUTIONS
test_start_4 = perf_counter()
for x in cases_my:
    algorithm(x)
test_stop_4 = perf_counter()
final_mine = test_stop_4 - test_start_4

best_time = min(final_org, final_first, final_second, final_mine)
# -------- RESULTS
print(f'Original Time is: {final_org}')
print(f'First Solution Time is: {final_first}')
print(f'Second Solution Time is: {final_second}')
print(f'My Solution Time is: {final_mine}')
print('==='*15)

print(f'Best Time is: {best_time}')


def wrapper(fun, fun_2):
    n = 6  # items in list
    m = 10000  # repetitions
    lo = 0
    hi = 100
    cases = [random.sample(range(lo, hi), n) for i in range(m)]

    for i in cases:
        one = fun(i)
        # two = diff_sum(fun_2(i))
        two = fun_2(i)
        print(i)
        print('brute', one)
        print('nub0', two)
        print(one == two)

