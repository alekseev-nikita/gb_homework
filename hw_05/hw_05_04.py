# Необходимо вывести те элементы, значения которых больше предыдущего
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([value for idx, value in enumerate(src) if value > src[idx - 1] and idx != 0])
