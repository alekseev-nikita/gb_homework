def is_suitable(num):
    separated_num = []
    while num != 0:
        x = num % 10
        num //= 10
        if x != 0:
            separated_num.append(x)
    return sum(separated_num) % 7 == 0


def get_suitable_cubes(sample):
    return list(i for i in sample if is_suitable(i))


# список кубов
cubes = list(i ** 3 for i in range(1, 1001, 2))
print(cubes)

# список кубов, сумма чисел которых делиться на цело на 7
suitable_cubes = get_suitable_cubes(cubes)
print(suitable_cubes)
print(sum(suitable_cubes))

# список кубов + 17
cubes = list(i + 17 for i in cubes)
print(cubes)

# список кубов, сумма чисел которых делиться на цело на 7
suitable_cubes = get_suitable_cubes(cubes)
print(suitable_cubes)
print(sum(suitable_cubes))
