from functools import singledispatch


@singledispatch
def fn(a):
    return "Generic"


@fn.register(int)
def _(a):
    return "{} is an int".format(a)


@fn.register(str)
def _(a):
    return "{} is a str".format(a)


if __name__ == '__main__':
    print(fn((1, 1)))  # Generic
    print(fn(1))  # 1 is an int
    print(fn('a'))  # a is a str

