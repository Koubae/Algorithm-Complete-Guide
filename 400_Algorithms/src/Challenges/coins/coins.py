# -*- coding: utf-8 -*-
"""
@Author: Federico Bau
@Date: 01/08/2022


"""


def first_solution(coins: list) -> int:
    if len(coins) <= 1:
        return 1
    coins.sort()

    current_found = 0
    for coin in coins:
        if coin > current_found + 1:
            return current_found + 1
        current_found += coin
    return current_found + 1

if __name__ == '__main__':
    coins = [5, 7, 1, 1, 2, 3, 22]
    result = first_solution(coins)
    print(f'result {result}')
