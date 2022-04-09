def odd_nums(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            yield i


def odd_nums_small(n):
    return (i for i in range(1, n + 1) if i % 2 != 0)


odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print('+' * 25)
odd_to_15_small = odd_nums_small(15)
print(next(odd_to_15_small))
print(next(odd_to_15_small))
print(next(odd_to_15_small))
print(next(odd_to_15_small))
