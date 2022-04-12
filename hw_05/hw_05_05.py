# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном
# списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
def get_unique_with_set(lst):
    no_repeats = set()
    repeats = set()
    for num in lst:
        if num in repeats:
            continue
        if num in no_repeats:
            no_repeats.discard(num)
            repeats.add(num)
            continue
        no_repeats.add(num)
    return no_repeats


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [num for num in src if num in get_unique_with_set(src)]
print(result)
