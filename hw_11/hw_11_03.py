import re


class OnlyDigitsException(Exception):
    pass


def ask_number():
    nums = []
    while True:
        user_input = input('Number input: ')
        if user_input == 'stop':
            break
        re_digits = re.compile(r'^\d+$')
        try:
            if not re_digits.match(user_input):
                raise OnlyDigitsException('Допускаются только числа')
        except OnlyDigitsException as expt:
            print(expt)
            continue
        nums.append(int(user_input))
    return nums


n = ask_number()
print(n)
