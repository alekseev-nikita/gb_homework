from functools import wraps


def val_checker(validation):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            values = []
            for arg in args:
                if not validation(arg):
                    raise ValueError(f'wrong val {arg}')
                values.append(f'{arg}: {type(arg)}')
            for k, v in kwargs.items():
                if not validation(v):
                    raise ValueError(f'wrong val {k}={v}')
                values.append(f'{k}={v}: {type(v)}')
            print(f'{func.__name__}({", ".join(values)})')
            return func(*args, **kwargs)

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x=4, y=7):
    return x ** 3


print(calc_cube(9))
print(calc_cube(x=7))
#print(calc_cube(-6))
