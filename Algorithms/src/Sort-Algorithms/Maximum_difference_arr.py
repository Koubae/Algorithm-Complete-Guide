"""
    Python: Maximum combined difference in array, Python

    @ https://stackoverflow.com/questions/53041365/python-maximum-difference-between-elements-in-a-list

    @ https://math.stackexchange.com/a/3975296/841658
"""

# print(*maxDiffs([8, 4, 1, 2, 3, 7]))  # 25 [4, 1, 8, 2, 7, 3]
import itertools
from collections import deque

input_data = [int(x) for x in input().split(" ")]
input_data.sort()


def maximum_difference_sort(data: list, *, start_with_max):
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


print(combined_difference(maximum_difference_sort(input_data, start_with_max=True)))


# =================== < OTHER SOLUTION > =================== # 

def little_big_sort(l):
    s = sorted(l)
    result = []
    result.append(s.pop(0))

    while len(s):
        if s:
            result.insert(len(result), s.pop(-1))
        if s:
            result.insert(0, s.pop(-1))
        if s:
            result.insert(len(result), s.pop(0))
        if s:
            result.insert(0, s.pop(0))

    return result

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


def solution(l):
    return max(diff_sum(little_big_sort(l)), diff_sum(big_little_sort(l)))

# The brute force approach:

def brute_force(l):
    result = 0

    for i in itertools.permutations(l):
        if diff_sum(i) > result:
            result = diff_sum(i)

    return result

import random

n = 2 # items in list
m = 10000 # repetitions
lo = 0
hi = 100

cases = [random.sample(range(lo, hi),n) for i in range(m)]

for i in cases:
    assert brute_force(i) == solution(i), f'failure for case {i}'


# =================== < OTHER SOLUTION BAD > =================== # 

def sumDiffs(R): return sum(abs(a-b) for a,b in zip(R,R[1:]))

def maxDiffs(A):
    if len(A)<=2 : return sumDiffs(A),A
    S = sorted(A)
    first  = [S.pop(len(S)//2)]
    half   = len(S)//2
    lower  = S[:half]
    upper  = S[-half:]
    last   = S[half:-half]
    def interlace(L,R): return [n for ab in zip(L,R) for n in ab]
    patterns = []
    for L,R in [(lower,upper),(upper,lower)]:
        for ld,rd in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            patterns.append(first + interlace(L[::ld],R[::rd]) + last)
    return max( (sumDiffs(p),p) for p in patterns ) 
                
print(*maxDiffs([8, 4, 1, 2, 3]))     # 17 [3, 1, 8, 2, 4]
print(*maxDiffs([8, 4, 1, 2, 3, 7]))  # 25 [4, 1, 8, 2, 7, 3]


from itertools import permutations
def bruteForce(A):
    return max( (sumDiffs(P),P) for P in permutations(A) )

import random
for size in range(1,101):
    failedCount = 0
    for i in  range(10):
        A = list(random.randrange(size*size) for _ in range(size))
        bfSum,bfValues = bruteForce(A)
        maxSum,values  = maxDiffs(A)
        if maxSum!=bfSum:
           print(size,"failed:",bfSum,maxSum,bfValues,values)
           failedCount += 1
    print("size",size,"failed:",failedCount)

# size 1 failed: 0
# size 2 failed: 0
# size 3 failed: 0
# size 4 failed: 0
# size 5 failed: 0
# size 6 failed: 0
# size 7 failed: 0
# size 8 failed: 0
# size 9 failed: 0
# size 10 failed: 0
# size 11 failed: 0






# =================== < MY SOLUTIONS 1 > =================== # 

def create_pipes(input_list):

    max_pipe = list()
    min_pipe = list()

    while len(input_list) > 1:
        # ---------------  Left Side Max Pipe
        max_n = input_list.index(max(input_list))
        max_pipe.append(input_list.pop(max_n))

        # --------------- Right Side Min Pipe
        min_n = input_list.index(min(input_list))
        min_pipe.append(input_list.pop(min_n))
    if input_list:
        min_pipe.append(input_list.pop())
    return max_pipe, min_pipe


def print_pipes(max_p, min_p):
    if len(max_p) == len(min_p):
        for n in range(len(max_p)):
            print(f'|| {max_p[n]}   *   {min_p[n]} ||')
    else:
        for n in range(len(max_p)):
            print(f'|| {max_p[n]}   *   {min_p[n]} ||')
        print(f'||     *   {min_p[-1]} ||')


#
# pipes  = create_pipes(l_2)
# max_pipe, min_pipe = pipes

def difference_algo(max_p, min_p):

    max_comparison = len(min_p) - 1
    counter = 0  # NOTE: Counter reset each 4. Then adds +2 to offset
    offset = 0
    max_difference = 0

    for max_val in range(max_comparison):
        if counter == 4:
            counter = 0
            offset += 2

        for comparison in range(2):
            diff = max_p[max_val] - min_p[comparison+offset]
            max_difference += diff
            counter += 1
    if len(min_p) % len(max_p) == 0:  # NOTE: In list is uneven, needs a last comparison with both last values
        max_difference += max_p[-1] - min_p[-1]

    return max_difference



# =================== < MY SOLUTIONS 2 > =================== # 


def algorithm(input_list):

    max_pipe = list()
    min_pipe = list()
    max_difference = 0


    while len(input_list) > 1:
        # ---------------  Left Side Max Pipe
        max_n = input_list.index(max(input_list))
        max_pipe.append(input_list.pop(max_n))

        # --------------- Right Side Min Pipe
        min_n = input_list.index(min(input_list))
        min_pipe.append(input_list.pop(min_n))
    if input_list:
        min_pipe.append(input_list.pop())
    max_comparison = len(min_pipe) - 1
    counter = 0  # NOTE: Counter reset each 4. Then adds +2 to offset
    offset = 0


    for max_val in range(max_comparison):

        # --------------- Handle Clusters of calculations, which are each 4 steps
        if counter == 4:
            counter = 0
            offset += 2

        for comparison in range(2):
            diff = max_pipe[max_val] - min_pipe[comparison + offset]
            max_difference += diff
            counter += 1
    if len(min_pipe) % len(max_pipe) == 0:  # NOTE: In list is uneven, needs a last comparison with both last values
        max_difference += max_pipe[-1] - min_pipe[-1]

    return max_difference

# =================== < MY SOLUTIONS 2 Improved > =================== # 


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