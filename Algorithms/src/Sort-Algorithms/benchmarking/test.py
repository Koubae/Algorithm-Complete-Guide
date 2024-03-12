# max_diff_arr.py
import timeit


ORIGINAL = '''
from other import maximum_difference_sort, combined_difference,  wrapper
import random

n = 40  # items in list
m = 10000  # repetitions
lo = 0
hi = 100
cases = [random.sample(range(lo, hi), n) for i in range(m)]

for i in cases:
    
    i.sort()
    combined_difference(maximum_difference_sort(i, start_with_max=True))

'''

FIRST_SOLUTION = '''
from other import maxDiffs
import random

n = 40  # items in list
m = 10000  # repetitions
lo = 0
hi = 100
cases = [random.sample(range(lo, hi), n) for i in range(m)]

for i in cases:
    maxDiffs(i)

'''

SECOND_SOLUTION = '''
from other import big_little_sort, diff_sum
import random

n = 40  # items in list
m = 10000  # repetitions
lo = 0
hi = 100
cases = [random.sample(range(lo, hi), n) for i in range(m)]

for i in cases:
    diff_sum(big_little_sort(i))

'''

MY_SOLUTION  = '''
from other import algorithm


import random

n = 40 # items in list
m = 10000  # repetitions
lo = 0
hi = 100
cases = [random.sample(range(lo, hi), n) for i in range(m)]

for i in cases:
    algorithm(i)
'''

original = min(timeit.Timer(ORIGINAL).repeat(1, 50))
first_solution = min(timeit.Timer(FIRST_SOLUTION).repeat(1, 50))
second_solution = min(timeit.Timer(SECOND_SOLUTION).repeat(1, 50))
my_solution = min(timeit.Timer(MY_SOLUTION).repeat(1, 50))
best_time = min(original, first_solution, second_solution, my_solution)

print(f'Original Time = {original}')
print(f'First Solution Time = {first_solution}')
print(f'Second Solution Time = {second_solution}')
print(f'My Solution = {my_solution}')
print('==='*15)

print(f'Best Time is: {best_time}')

