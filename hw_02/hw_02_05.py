prices = [57.8, 46.51, 97, 54.2, 32, 225, 23.65, 32.0, 97.1]
readable_prices = []
for value in prices:
    value = str(float(value)).split('.')
    readable_prices.append(f'{value[0]} руб {int(value[1]):02d} коп')
print(', '.join(readable_prices))
print(f'До сортировки id = {id(prices)}')
prices.sort()
print(f'После сортировки id = {id(prices)}')
print(prices)
reverse_prices = sorted(prices, reverse=True)
print(reverse_prices)
print(f'5 самых дорогих: {reverse_prices[0:5]}')
