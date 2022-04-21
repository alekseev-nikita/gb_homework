from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        values = []
        for arg in args:
            values.append(f'{arg}: {type(arg)}')
        for k, v in kwargs.items():
            values.append(f'{k}={v}: {type(v)}')
        print(f'{func.__name__}({", ".join(values)})')
        return func(*args, **kwargs)
    return wrapper


@type_logger
def calc_cube(x=4, y=2):
    return (x**3), (y**3)


a = calc_cube(x=3, y=4)
print(a)
