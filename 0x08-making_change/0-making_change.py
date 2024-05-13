#!/usr/bin/python3
"""Defining a function makeChange"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """returns the minimum number of coins to reach the desired total"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    total_coins = 0
    total_value = 0

    while total_value != total:
        if not coins:
            return -1

        max_coin = coins[0]
        if total_value + max_coin > total:
            coins.pop(0)
        else:
            total_value += max_coin
            total_coins += 1

    return total_coins
