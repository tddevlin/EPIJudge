from test_framework import generic_test
from epi_judge_python.buy_and_sell_stock import buy_and_sell_stock_once


# def buy_and_sell_stock_twice(prices):
#     best_profit = 0
#     for i in range(len(prices)):
#         left_prices = prices[:i]
#         right_prices = prices[i:]
#         profit = buy_and_sell_stock_once(left_prices) + buy_and_sell_stock_once(right_prices)
#         if profit > best_profit:
#             best_profit = profit
#     return best_profit


def buy_and_sell_stock_twice(prices):
    profit_selling_by_date = [0] * len(prices)
    profit_buying_after_date = [0] * len(prices)
    highest_price = 0
    best_profit = 0
    for i in range(len(prices)-1, -1, -1):
        if prices[i] > highest_price:
            highest_price = prices[i]
        profit = highest_price - prices[i]
        if profit > best_profit:
            best_profit = profit
        profit_buying_after_date[i] = best_profit
    lowest_price = float('inf')
    best_profit = 0
    for i in range(len(prices)):
        if prices[i] < lowest_price:
            lowest_price = prices[i]
        profit = prices[i] - lowest_price
        if profit > best_profit:
            best_profit = profit
        profit_selling_by_date[i] = best_profit
    best_total_profit = 0
    for i in range(len(prices)-1):
        total_profit = profit_selling_by_date[i] + profit_buying_after_date[i]
        if total_profit > best_total_profit:
            best_total_profit = total_profit
    return best_total_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
