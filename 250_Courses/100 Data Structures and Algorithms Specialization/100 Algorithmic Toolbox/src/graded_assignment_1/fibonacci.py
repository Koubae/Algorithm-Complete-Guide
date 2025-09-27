def fibonacci_number_original(n):
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


def fibonacci_number(n):
    if n <= 1:
        return n
    nums = [0, 1]
    for i in range(2, n + 1):
        a = nums[i - 1]
        b = nums[i - 2]
        nums.append(a + b)
    return nums[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
    # print(fibonacci_number_original(input_n))

