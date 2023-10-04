'''
File: IBM-task-schedular.py
Project: Coding
File Created: 26th Sep 2023 10:38 pm, Tuesday
Author: Saurabh Zinjad (GitHub: Ztrimus)
Email: zinjadsaurabh1997@gmail.com

Copyright (c) 2023 Saurabh Zinjad
'''

def getMaximumProfit(price, profit):
    n = len(price)

    # Initialize arrays to store maximum profits for each day
    max_profit_left = [0] * n
    max_profit_right = [0] * n

    # Calculate maximum profits for each day considering past days
    max_profit_left[0] = profit[0]
    for i in range(1, n):
        max_profit_left[i] = max(max_profit_left[i - 1], profit[i])

    # Calculate maximum profits for each day considering future days
    max_profit_right[n - 1] = profit[n - 1]
    for i in range(n - 2, -1, -1):
        max_profit_right[i] = max(max_profit_right[i + 1], profit[i])

    max_total_profit = -1

    # Find the maximum total profit for a valid triplet
    for i in range(1, n - 1):
        if price[i - 1] < price[i] < price[i + 1]:
            total_profit = profit[i] + max_profit_left[i - 1] + max_profit_right[i + 1]
            max_total_profit = max(max_total_profit, total_profit)

    return max_total_profit
