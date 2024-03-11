def myfunc(*args):
    for item in args:
        print(item)
    return sum(args) * 0.05


print(myfunc(40, 60, 100, 1, 34))


def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


myfunc(fruit='apple', veggie='lettuce')


def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']))


myfunc(10, 20, 30, fruit='orange', food='egg', animal='dog')

