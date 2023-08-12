def add(*args):
    print(args)
    sum = 0
    for n in args:
        sum += n
    return sum


add(3, 5, 6)


def calculate(**kwargs):
    print(kwargs)


add(3, 2, 1, 4, 7, 6, 4)
calculate(add=3, multiply=5)
