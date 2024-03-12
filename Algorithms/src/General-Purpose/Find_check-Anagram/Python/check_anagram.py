"""
    Check if 2 Words are Anagrams.

    @Author: Federico Baù
    @Date: 1/18/2021
    @Updated: N/A
    ------------------

    Note:

    Resources:
        * Check if two unordered lists are equal:
            https://stackoverflow.com/questions/9623114/check-if-two-unordered-lists-are-equal
        * How to efficiently compare two unordered lists (not sets) in Python?:
            https://stackoverflow.com/questions/7828867/how-to-efficiently-compare-two-unordered-lists-not-sets-in-python
        * An Anagram Detection Example:
            https://runestone.academy/runestone/books/published/pythonds3/AlgorithmAnalysis/AnAnagramDetectionExample.html


"""

import collections
from time import perf_counter

# ================== < ANAGRAM WORDS COUPLES> ================== #
tar_rat = ('tar', 'rat')
arc_car = ('arc', 'car')
elbow_below = ('elbow', 'below')
state_taste = ('state', 'taste')
cider_cried = ('cider', 'cried')
dusty_study = ('dusty', 'study')
night_thing = ('night', 'thing')
inch_chin = ('inch', 'chin')
brag_grab = ('brag', 'grab')
cat_act = ('cat', 'act')
bored_robed = ('bored', 'robed')
save_vase = ('save', 'vase')
angel_glean = ('angel', 'glean')
stressed_desserts = ('stressed', 'desserts')
ANAGRAM_COUPLES = [tar_rat, arc_car, elbow_below, state_taste, cider_cried, dusty_study,
                   night_thing, inch_chin, brag_grab, cat_act, bored_robed, save_vase,
                   angel_glean, stressed_desserts]


def tester_check(words_tuples, test_function, is_lambda=False):

    for word_couple in words_tuples:
        if is_lambda:
            if not test_function(*word_couple):
                print('==='*15)
                print('TEST FAILED')
            else:
                pass
        else:
            if not test_function(word_couple):
                print('==='*15)
                print('TEST FAILED')
            else:
                pass


def tester_benchmark(words_tuples, test_function, is_lambda=False):
    """

    :param words_tuples (tuple): List of Anagram words to check
    :param test_function: Function to test the performance
    :return: float  Total elapsed time in which the function had found the Anagram
    """
    if not is_lambda:
        start = perf_counter()
        for times in range(0, 100_000):
            for word_couple in words_tuples:
                test_function(word_couple)
        end = perf_counter()
        return end-start
    else:
        start = perf_counter()
        for times in range(0, 100_000):
            for word_couple in words_tuples:
                test_function(*word_couple)
        end = perf_counter()
        return end - start


# ================== < USING SET COMPARISON + LEN > ================== #
def anagram_set_001(words):
    """ Check if a Tuple of words are Anagrams

        NOTE: Technically, using set you won't check for double words, by checking the lenght first
        you are guaranteed to find the correct answer, for instance stressed, desserts.
            1. Checks first the length.
            2. Makes it a set, removes the double s so stresed, deserts
        However, it will fails if  words are streseed, desserts. as set will turn to stresed, deserts which is incorrect
    :param words: Tuple
    :return: bool
    """
    word_one, word_two = words
    if len(word_one) != len(word_two):
        return False
    else:
        return set(word_one) == set(word_two)

anagram_set_001_lambda = lambda x, v: len(x) == len(v) and set(x) == set(v)
tester_check(ANAGRAM_COUPLES, anagram_set_001)
tester_check(ANAGRAM_COUPLES, anagram_set_001_lambda, is_lambda=True)


# ================== < USING Counter - Compare > ================== #
def compare_function(words):
    """ Check if a Tuple of words are Anagrams
        NOTE: This solution solves the issue of duplicate char
    :param words: Tuple
    :return: bool
    """
    word_one, word_two = words
    return collections.Counter(word_one) == collections.Counter(word_two)

compare_lambda = lambda x, y: collections.Counter(x) == collections.Counter(y)
tester_check(ANAGRAM_COUPLES, compare_function)
tester_check(ANAGRAM_COUPLES, compare_lambda, is_lambda=True)


# ================== < USING List Sorted > ================== #
def list_sort(words):
    """ Check if a Tuple of words are Anagrams using Sort on place
    :param words: Tuple
    :return: bool
    """
    word_one, word_two = words
    word_one = list(word_one)
    word_one.sort()

    word_two = list(word_one)
    word_two.sort()
    return word_one == word_two


def list_sorted(words):
    """ Check if a Tuple of words are Anagrams using Sorted
    :param words: Tuple
    :return: bool
    """
    word_one, word_two = words

    return sorted(word_one) == sorted(word_two)


list_sorted_lambda = lambda word_one, word_two: sorted(word_one) == sorted(word_two)
tester_check(ANAGRAM_COUPLES, list_sort)
tester_check(ANAGRAM_COUPLES, list_sorted)
tester_check(ANAGRAM_COUPLES, compare_lambda, is_lambda=True)


# ===================================================================================== #
        # ================== < runestone.academy SOLUTIONS > ================== #
# ************************************************************************************* #

# ===================================================================================== #


# ================== < Solution 1: Checking Off > ================== #
def anagram_solution_1(words):
    """ Complexity O(n2)
        If it is possible to “checkoff” each character, then the two strings must be anagrams
    :param words: Tuple
    :return: bool
    """
    s1, s2 = words
    still_ok = True
    if len(s1) != len(s2):
        still_ok = False

    a_list = list(s2)
    pos_1 = 0

    while pos_1 < len(s1) and still_ok:
        pos_2 = 0
        found = False
        while pos_2 < len(a_list) and not found:
            if s1[pos_1] == a_list[pos_2]:
                found = True
            else:
                pos_2 = pos_2 + 1

        if found:
            a_list[pos_2] = None
        else:
            still_ok = False

        pos_1 = pos_1 + 1

    return still_ok


tester_check(ANAGRAM_COUPLES, anagram_solution_1)
# ================== <  Solution 2: Sort and Compare > ================== #
def anagram_solution_2(words):
    """
    Sort and Compare Complexity O(nlogn)
    :param words: Tuple
    :return: bool
    """
    s1, s2 = words
    a_list_1 = list(s1)
    a_list_2 = list(s2)

    a_list_1.sort()
    a_list_2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if a_list_1[pos] == a_list_2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


tester_check(ANAGRAM_COUPLES, anagram_solution_2)

# ================== < Solution 4: Count and Compare > ================== #
def anagram_solution_4(words):
    """
        Count and Compare Complexity O(n)
        Although the last solution was able to run in linear time,
        it could only do so by using additional storage to keep the two lists of character counts.
        In other words, this algorithm sacrificed space in order to gain time.
        :param words: Tuple
        :return: bool
    """
    s1, s2 = words
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord("a")
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord("a")
        c2[pos] = c2[pos] + 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False

    return still_ok


tester_check(ANAGRAM_COUPLES, anagram_solution_4)


# ================== < BENCHMARK TESTS | NAIVE TEST > ================== #

# -------- Test anagram_set_001
test_anagram_set_001 = tester_benchmark(ANAGRAM_COUPLES, anagram_set_001)
print(f'Test for anagram_set_001, Total Time = {test_anagram_set_001}')

# -------- Test anagram_set_001_lambda
test_anagram_set_001_lambda = tester_benchmark(ANAGRAM_COUPLES, anagram_set_001_lambda, is_lambda=True)
print(f'Test for anagram_set_001_lambda, Total Time = {test_anagram_set_001_lambda}')

# -------- Test compare_function
test_compare_function = tester_benchmark(ANAGRAM_COUPLES, compare_function)
print(f'Test for compare_function, Total Time = {test_compare_function}')

# -------- Test compare_lambda
test_compare_lambda = tester_benchmark(ANAGRAM_COUPLES, compare_lambda, is_lambda=True)
print(f'Test for compare_lambda, Total Time = {test_compare_lambda}')


# -------- Test list_sort
test_list_sort = tester_benchmark(ANAGRAM_COUPLES, list_sort)
print(f'Test for list_sort, Total Time = {test_list_sort}')

# -------- Test list_sorted
test_list_sorted = tester_benchmark(ANAGRAM_COUPLES, list_sorted)
print(f'Test for list_sorted, Total Time = {test_list_sorted}')

# -------- Test list_sorted_lambda
test_list_sorted_lambda = tester_benchmark(ANAGRAM_COUPLES, list_sorted_lambda, is_lambda=True)
print(f'Test for list_sorted_lambda, Total Time = {test_list_sorted_lambda}')

# ================== < runestone.academy SOLUTIONS > ================== #
# -------- Test anagram_solution_1
test_anagram_solution_1 = tester_benchmark(ANAGRAM_COUPLES, anagram_solution_1)
print(f'Test for anagram_solution_1, Total Time = {test_anagram_solution_1}')

# -------- Test anagram_solution_2
test_anagram_solution_2 = tester_benchmark(ANAGRAM_COUPLES, anagram_solution_2)
print(f'Test for anagram_solution_2, Total Time = {test_anagram_solution_2}')

# -------- Test anagram_solution_4
test_anagram_solution_4 = tester_benchmark(ANAGRAM_COUPLES, anagram_solution_4)
print(f'Test for anagram_solution_4, Total Time = {test_anagram_solution_4}')

result = {'test_anagram_set_001': test_anagram_set_001,
          'test_anagram_set_001_lambda': test_anagram_set_001_lambda,
          'test_compare_function': test_compare_function,
          'test_compare_lambda': test_compare_lambda,
          'test_list_sort': test_list_sort,
          'test_list_sorted': test_list_sorted,
          'test_list_sorted_lambda': test_list_sorted_lambda,
          'test_anagram_solution_1': test_anagram_solution_1,
          'test_anagram_solution_2': test_anagram_solution_2,
          'test_anagram_solution_4': test_anagram_solution_4}

result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}
print(result)
# TODO:
    # 1 Check if save length
    # 2 Check if they all have same letters


# Test for anagram_set_001, Total Time = 0.994643
# Test for anagram_set_001_lambda, Total Time = 0.9844885999999999
# Test for compare_function, Total Time = 3.6090758
# Test for compare_lambda, Total Time = 3.6017713999999996
# Test for list_sort, Total Time = 0.8287557000000003
# Test for list_sorted, Total Time = 0.9058220000000006
# Test for list_sorted_lambda, Total Time = 0.8824179999999995
# Test for anagram_solution_1, Total Time = 3.788814800000001
# Test for anagram_solution_2, Total Time = 1.6267801000000013
# Test for anagram_solution_4, Total Time = 5.775225499999998
# {'test_list_sort': 0.8287557000000003, 'test_list_sorted_lambda': 0.8824179999999995, 'test_list_sorted': 0.9058220000000006,
# 'test_anagram_set_001_lambda': 0.9844885999999999,
# 'test_anagram_set_001': 0.994643, 'test_anagram_solution_2': 1.6267801000000013,
# 'test_compare_lambda': 3.6017713999999996, 'test_compare_function': 3.6090758,
# 'test_anagram_solution_1': 3.788814800000001, 'test_anagram_solution_4': 5.775225499999998}


