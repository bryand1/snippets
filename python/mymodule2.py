from functools import wraps


def positive(fn):
    @wraps(fn)
    def wrapper(*args):
        if any(map(lambda x: x < 0, args)):
            return
        return fn(*args)
    return wrapper


@positive
def add(x, y):
    """Add two values"""
    return x + y


@positive
def sub(x, y):
    """Subtract two values"""
    return x - y
