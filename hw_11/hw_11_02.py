class ZeroDivSoft(ZeroDivisionError):
    pass


def calc(x, y):
    try:
        if y == 0:
            raise ZeroDivSoft()
        z = x / y
    except ZeroDivSoft:
        print('Next time')
    return z


calc(2, 2)
