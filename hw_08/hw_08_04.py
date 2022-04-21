from functools import wraps


def val_checker(validation):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            values = []
            for arg in args:
                if not validation(arg):
                    raise ValueError(f'wrong val {arg}')
                values.append(f'{arg}: {type(arg)}')
            print(f'{func.__name__}({", ".join(values)})')
            return func(*args)

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(4))
print(calc_cube(-6))
