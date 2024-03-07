stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53,
                47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
    price = stock_prices[x - 1]
    return price

def max_prices(a, b):
    start = stock_prices[a - 1]
    end = stock_prices[b - 1]
    max_price = max(start, end)
    return max_price

def min_prices(a, b):
    start = stock_prices[a - 1]
    end = stock_prices[b - 1]
    min_price = min(start, end)
    return min_price

print(price_at(7))
print(max_prices(2, 18))
print(min_prices(6, 19))