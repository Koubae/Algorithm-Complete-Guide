def linear_search(values, target):
    """
    Complexity : O(n)

    Args:
        values (list):
        target (int ):

    Returns:
        string : Value not found
        int : Target value found
    """

    for n in values:
        if n == target:
            return n
    return "Not Found"


if __name__ == '__main__':
    # Linear Search
    nums = list(range(1, 11)) # 1 --> 10 nums
    test_1 = 12
    print(f"Test for n {test_1} --> {linear_search(nums, test_1)}")

    test_1 = 6
    print(f"Test for n {test_1} --> {linear_search(nums, test_1)}")

    test_1 = 7
    print(f"Test for n {test_1} --> {linear_search(nums, test_1)}")