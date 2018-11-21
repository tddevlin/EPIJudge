from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    best_profit = 0
    max_price = prices[-1]
    for price in reversed(prices):
        max_price = max(max_price, price)
        best_profit = max(best_profit, max_price - price)
    return best_profit

# def buy_and_sell_stock_once(prices):
#     best_profit = 0
#     best_price = 0
#     for i in range(len(prices)-1, -1, -1):
#         if prices[i] > best_price:
#             best_price = prices[i]
#         profit = best_price - prices[i]
#         if profit > best_profit:
#             best_profit = profit
#     return best_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
